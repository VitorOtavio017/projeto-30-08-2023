from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import Http404
from django.shortcuts import redirect, render 
from django.urls import reverse
from .forms import LoginForm, RegisterForm
from authors.forms import RegisterForm

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
# def register_login(request):
#    if not request.POST:
#       raise Http404()
   
#    form = RegisterForm(request.POST)
#    return render(request, 'pages/register.html', context={
#                  'form': form,
#    })
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



