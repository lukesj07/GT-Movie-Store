from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm, CustomErrorList


def signup(request: HttpRequest) -> render: 
    template_data = {}
    template_data['title'] = 'Sign Up'
    
    # provide the view of the form
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html',
                      {'template_data': template_data})
    elif request.method == 'POST':
        # if submitting the form, then we save the user into the database and redirect to the home page
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')
        else:
            # display form with errors
            template_data['form'] = form
            return render(request, 'accounts/signup.html',
                      {'template_data': template_data})


def login(request: HttpRequest):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'accounts/login.html', 
                      {'template_data' : template_data})
    elif request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password'],
        )
        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request,
                'accounts/login.html',
                {'template_data': template_data})
        else:
            auth_login(request, user)
            return redirect('home.index')
        

@login_required
def logout(request: HttpRequest) -> redirect:
    auth_logout(request)
    return redirect('home.index')