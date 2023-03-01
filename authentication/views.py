from django.shortcuts import render,redirect
#from django.contrib.auth.models import Group, User
# from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
#from django.contrib.auth.decorators import login_required
#from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from.forms import ApplicationForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('login')
            else:
                return redirect('signup')
    else:
        form = ApplicationForm()
    return render(request=request, templates_name='authentication/signup.html', context={'form_data': form})

def login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, "You are now logged in as {username}.")
				return redirect("templates:base")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="templates/home.html", context={"form_data":form})



def logout(request):
    logout(request)
    messages.info(request, 'You have successfully log out.')
    return redirect('templates:home')
