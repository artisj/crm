from django.shortcuts import render, HttpResponse, redirect

from .forms import CreateUserForm
from .models import Customer
# to send messages to users
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

# Create your views here.
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        #gets post data
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            #gets data from the form, to display when account is created
            username = form.cleaned_data.get('username')

            Customer.objects.create(user=user, name=user.username)
            #send message to form
            messages.success(request,
                             'Account has been created for ' + username)
            redirect('login')

    return render(request, 'Accounts/register.html', {'form': form})

def loginPage(request):
  if request.method == 'POST':
    #username in get is the value from the form variable name
    username = request.POST.get('username')
    password = request.POST.get('password')

    #Django authenticate
    user = authenticate(request,username=username, password=password)

    if user is not None:
      login(request, user)
      return HttpResponse("Logged in")
    else:
      messages.info(request, 'Username or password is incorect')
  return render(request, 'Accounts/login.html', {})

def logoutUser(request):
  logout(request)
  return redirect('login')
