from django.contrib import messages
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
      form.save()
      messages.success(request, 'Seu usuário foi criado, por favor faça o login')
      del(request.session['register_form_data'])


   form = RegisterForm(POST)
   return redirect('authors-register')

def login(request):
    form = LoginForm()
    return render(request, 'pages/login.html', {
        'form': form,
        'form_action': reverse('authors-login-create')
    })

def login_create(request):
    return render(request, 'pages/login.html')



