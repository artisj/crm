from django.shortcuts import render, HttpResponse, redirect

from .forms import CreateUserForm, OrderForm
from .models import Customer, Product, Tag, Order
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

def homePage(request):
  orders = Order.objects.all()
  customers = Customer.objects.all()

  total_customers= customers.count()
  total_orders = orders.count()

  delivered = orders.filter(status='Delivered').count()
  pending = orders.filter(status='Pending').count()

  context = {'orders':orders, 'customers': customers,
            'total_orders':total_orders, 'total_customers':total_customers,'delivered':delivered, 'pending':pending}

  return render(request, 'Accounts/dashboard.html', context)

def updateOrder(request, pk):
  form = OrderForm()
  order = Order.objects.get(id=pk)
  
  if request.method == 'POST':
    # this creates the instance of form and adds previous data
    form = OrderForm(request.POST, instance = order)
    if form.is_valid():
      form.save()
      return redirect('/')
  context ={'form': form}
  return render(request, 'Accounts/order_form.html', context)

def deleteOrder(request):
  pass
