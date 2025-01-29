from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm, CustomErrorList
from django.http import HttpRequest


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
            return redirect('home.index')
        else:
            # display form with errors
            template_data['form'] = form
            return render(request, 'accounts/signup.html',
                      {'template_data': template_data})