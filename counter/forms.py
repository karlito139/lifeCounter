from django import forms


class NewUserForm(forms.Form):
    birthdayDate = forms.CharField(label='Birth date', max_length=20)
    email = forms.EmailField(label='Email', max_length=100)

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)