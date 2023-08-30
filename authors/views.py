from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import Http404
from django.shortcuts import redirect, render 
from django.urls import reverse
from .forms import LoginForm, RegisterForm, AuthorPostForm
from authors.forms import RegisterForm
from mural.models import Mural

# Create your views here.

def register_register(request):
    #Dessa forma é criado uma variável com o mesmo nome do valor de session
    #Caso seja vazio vem None (Por isso de none após a vírgula)
    #Get = pegar é o contrário do POST, mas ai ele já está pegando os dados. Pois o 0 redirect é GET
    register_from_data = request.session.get('register_form_data', None)

    #Ai é passado as informações para dentro do Form da página
    form = RegisterForm(register_from_data)
    return render(request, 'pages/register.html', context={
        'form': form,
    })

def register_create(request):
   if not request.POST:
      raise Http404()
   
   POST = request.POST
   request.session['register_form_data'] = POST


   form = RegisterForm(POST)

   if form.is_valid():
       data = form.save(commit=False)
       password = request.POST['password']
       data.password = make_password(data.password)
       data.save()
       messages.success(request, 'Seu usuário foi criado, por favor faça o login')
       del(request.session['register_form_data'])   
       return redirect(reverse('authors-login'))


   return redirect('authors-register')

def login_view(request):
    form = LoginForm()
    return render(request, 'pages/login.html', {
        'form': form,
        'form_action': reverse('authors-login-create')
    })

def login_create(request):
     
     if not request.POST:
         raise Http404
     
     form = LoginForm(request.POST)
     login_url = reverse('authors-login')

     if form.is_valid():
         
        authenticated_user = authenticate(
             username=form.cleaned_data.get('username', ''),
             password=form.cleaned_data.get('password', ''),
         )

        if authenticated_user is not None:
            messages.success(request, 'Sucesso, você logou')

            login(request, authenticated_user)
            return redirect(reverse("projeto-menu"))

        else:
          
          messages.error(request, 'Usuário ou senha estão incorretos')
    
     else:
        
        messages.error(request, "Credencias Inválidas")

     return redirect(login_url)

     


     return render(request, 'pages/login.html')
@login_required(login_url='authors-login', redirect_field_name='next')
def logout_view(request):

    if not request.POST:

        return redirect(reverse('authors-login'))
    

    if request.POST.get('username') != request.user.username:
        return redirect(reverse('authors-login'))

    logout(request)

    return redirect(reverse('authors-login'))

@login_required(login_url='authors-login', redirect_field_name='next')
def projetos(request):
    cards = Mural.objects.filter(is_published=False, usuario=request.user)
    return render(request, 'pages/mycards.html', context={
        'cards': cards,
    })



@login_required(login_url='authors-login', redirect_field_name='next')
def projetos_card_edit(request, id):
    card = Mural.objects.filter(
        is_published=False,
        usuario=request.user,
        pk=id,
    ).first()
    
    if not card:
        raise Http404()
    
    form = AuthorPostForm(
        request.POST or None,
        instance=card
    )
    
    if form.is_valid():
        card = form.save(commit=False)

        card.usuario = request.user
        card.is_published = False
        
        card.save()

        messages.success(request, 'Sua postagem foi salva com sucesso!')

        return redirect(reverse('authors-projetos-card-edit', args= (id,)))


    return render(request, 'pages/create_card.html', context={
        'cards':card,
        'form' :form,
        
    })
@login_required(login_url='authors-login', redirect_field_name='next')
def projetos_card_new(request):
    form = AuthorPostForm(
        data=request.POST or None,
    )
    
    if form.is_valid():
        card: Mural = form.save(commit=False)

        card.usuario = request.user
        # card.oferece_ajuda = False
        
        card.save()

        messages.success(request, 'Salvo com sucesso!')

        return redirect(reverse('authors-projetos-card-edit', args= (card.id,)))
    
    return render(request, 'pages/create_card.html', context={
        'form' :form,
        'form_action': reverse('authors-projetos-card-new')
        
    })


@login_required(login_url='authors-login', redirect_field_name='next')
def projetos_card_delete(request):

    if not request.POST:
        raise Http404()
    
    POST = request.POST
    id = POST.get('get')

    card = Mural.objects.filter(
        # oferece_ajuda=False,
        usuario=request.user,
        pk=id
    ).filter()

    if not card:
        raise Http404()
    card.delete()
    messages.success(request, 'Postagem deletada com successo.')
    return redirect(reverse('authors-projetos'))





