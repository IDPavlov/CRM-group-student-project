from django.shortcuts import render
from .forms import RegistrationForm
from .models import CrmUser


def main_view(request):
    message = 'This message is in the code (server.views)'
    return render(request, 'server/main.html', {
        'message': message
    })

def registration_view(request):
    is_success = False
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = CrmUser(
                username=data['username'],
                email=data['email']
            )
            user.set_password(data['password'])
            user.save()
            print(form.cleaned_data)
            is_success = True
    return render(request, 'server/registration.html', {
        'form': form,
        'is_success': is_success
    })
