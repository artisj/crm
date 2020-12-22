from django.shortcuts import render, HttpResponse

from .forms import CreateUserForm
from .models import Customer
# to send messages to users
from django.contrib import messages


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
            #return HttpResponse('Sucess')

    return render(request, 'Accounts/register.html', {'form': form})
