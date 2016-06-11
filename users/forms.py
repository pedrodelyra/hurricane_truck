from django import forms
from django.core.validators import validate_email
from django.core.validators import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class SignupForm(forms.ModelForm):
	username = forms.CharField(max_length=128, required=True)
	email = forms.CharField(max_length=128, required=True, validators=[validate_email])
	password = forms.CharField(label="password", min_length=6, max_length=64, widget=forms.PasswordInput, required=True)
	password_confirmation = forms.CharField(label="password_confirmation", min_length=6, max_length=64, widget=forms.PasswordInput, required=True)

	def clean_password(self):
		password = self.data['password']
		password_confirmation = self.data['password_confirmation']
		if password != password_confirmation:
			self._errors['password'] = self.error_class(['Confirmation does not match password'])
		return password

	class Meta:
		model = User
		fields = ('username', 'email', 'password')
