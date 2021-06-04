from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models.signals import post_save
from Book_Store.models import User_customer,StoreUser

class RegistrationForm(UserCreationForm):

	class Meta:
		model=User
		fields=(
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
			)

		widgets = {
			'username': forms.TextInput(attrs={'class': 'text','placeholder': 'Enter the user name'}),
			'first_name':forms.TextInput(attrs={'class': 'text','placeholder': 'Enter your First name'}),
			'last_name':forms.TextInput(attrs={'class': 'text','placeholder': 'Enter your Last name'}),
			'email':forms.TextInput(attrs={'class': 'text email','placeholder': 'Enter your email'}),
			'password1':forms.PasswordInput(attrs={'class': 'text','placeholder': 'Password'}),
			'password2': forms.PasswordInput(attrs={'class': 'text w3lpass','placeholder': 'Re-password'}),
		}

	def save(self,commit=True):
		user=super(RegistrationForm,self).save(commit=False)
		user.first_name=self.cleaned_data['first_name']
		user.last_name=self.cleaned_data['last_name']
		user.email=self.cleaned_data['email']

		if commit:
			def create_profilee(sender, **kwargs):
				if kwargs['created']:
					User_customer.objects.create(user=kwargs['instance'])
			post_save.connect(create_profilee, sender=User)
			user.save()
		return user
class StoreRegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
		)

		widgets = {
			'username': forms.TextInput(attrs={'class': 'text','placeholder': 'Enter the user name'}),
			'first_name':forms.TextInput(attrs={'class': 'text','placeholder': 'Enter your First name'}),
			'last_name':forms.TextInput(attrs={'class': 'text','placeholder': 'Enter your Last name'}),
			'email':forms.TextInput(attrs={'class': 'text email','placeholder': 'Enter your email'}),
			'password1':forms.PasswordInput(attrs={'class': 'text','placeholder': 'Password'}),
			'password2': forms.PasswordInput(attrs={'class': 'text w3lpass','placeholder': 'Re-password'}),
		}

	def save(self, commit=True):
		user = super(StoreRegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		user.is_staff = True

		if commit:
			def create_profile(sender, **kwargs):
				if kwargs['created']:
					Store_User=StoreUser.objects.create(user=kwargs['instance'])

			post_save.connect(create_profile, sender=User)
			user.save()
		return user
