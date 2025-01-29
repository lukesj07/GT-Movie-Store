from django.shortcuts import redirect, render

# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm

def signup(request: HttpRequest) -> render: 
    template_data = {}
    template_data['title'] = 'Sign Up'
    
    # provide the view of the form
    if request.method == 'GET':
        template_data['form'] = UserCreationForm()
        return render(request, 'accounts/signup.html',
                      {'template_data': template_data})
    elif request.method == 'POST':
        # if submitting the form, then we save the user into the database and redirect to the home page
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home.index')
        else:
            # display form with errors
            template_data['form'] = form
            return render(request, 'accounts/signup.html',
                      {'template_data': template_data})