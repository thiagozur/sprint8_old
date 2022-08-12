from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder' : 'Usuario', 'class' : 'form-control'}))
    password = forms.CharField(label='', required=True, max_length=100, widget=forms.PasswordInput(attrs={'placeholder' : 'Contraseña', 'class' : 'form-control', 'type' : 'password', 'id' : 'pass'}))