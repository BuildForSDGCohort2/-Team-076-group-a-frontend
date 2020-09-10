from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import UserAccount


# User = get_user_model()

class LoginForm(forms.ModelForm):
	email = forms.EmailField()
	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = UserAccount
		fields = ('email', 'password')


	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")



#registration form
class RegistrationForm(UserCreationForm):
	# email = forms.EmailField(max_length=60, label='Email', help_text='Required')
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
	password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())


	class Meta:
		model = UserAccount
		fields = ('username', 'email', 'first_name', 'last_name', 'address', 'status', 'phone_number')

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if password1 and password2 and password1 != password2:
			raise ValidationError("Passwords don't match")

		return password2

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user



class AccountUpdate(forms.ModelForm):

	class Meta:
		model = UserAccount
		fields = ('username', 'first_name', 'last_name', 'address', 'phone_number', 'email', 'profile_image')

	# def clean_password(self):
	# 	return self.initial['password']

	def clean_email(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			try:
				account = UserAccount.objects.exclude(pk=self.instance.pk).get(email=email)
			except UserAccount.DoesNotExist:
				return email
			raise forms.ValidationError('This email is in use')

	def clean_username(self):
		if self.is_valid():
			username = self.cleaned_data['username']
			try:
				account = UserAccount.objects.exclude(pk=self.instance.pk).get(username=username)
			except UserAccount.DoesNotExist:
				return username
			raise forms.ValidationError('This username is in use')


class VerifyNumber(forms.ModelForm):

	class Meta:
		model = UserAccount
		fields = ('phone_code',)





