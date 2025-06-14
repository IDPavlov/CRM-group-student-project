from django import forms

from crm.server.models import CrmUser


class RegistrationForm(forms.ModelForm):
    # email = forms.EmailField()
    # username = forms.CharField()
    # password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password_confirm']:
            self.add_error('password_confirm', 'Пароли не совпадают')
        return cleaned_data

    class Meta:
        model = CrmUser
        fields = ('email', 'username', 'password', 'password_confirm')