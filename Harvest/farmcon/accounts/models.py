from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django_resized import ResizedImageField


class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, first_name, last_name, address, status, phone_number, password=None):
		if not email:
			raise ValueError("User must have an email address")
		if not username:
			raise ValueError("User must have a username")
		if not first_name:
			raise ValueError("User must have a first name")
		if not last_name:
			raise ValueError("User must have a last name")
		if not address:
			raise ValueError('User must have an address')
		if not phone_number:
			raise ValueError('User must have a valid phone number')


		user = self.model(
				email = self.normalize_email(email),
				username = username,
				first_name = first_name,
				last_name = last_name,
				address = address,
				status = status,
				phone_number = phone_number
			)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, first_name, last_name, username, address, status, password, phone_number):
		user = self.create_user(
				email = self.normalize_email(email),
				password = password,
				username = username,
				first_name = first_name,
				last_name = last_name,
				address = address,
				status = status,
				phone_number = phone_number
			)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.is_active = True
		user.save(using=self._db)
		return user



STATUS_CHOICES = (
				('Buyer', 'Buyer'),
				('Farmer', 'Farmer'),
				)
class UserAccount(AbstractBaseUser):
	email						= models.EmailField(verbose_name='Email', max_length=60, unique=True)
	username					= models.CharField(max_length=30, unique=True)
	first_name					= models.CharField(max_length=15)
	last_name					= models.CharField(max_length=15)
	status 						= models.CharField(max_length=10, choices=STATUS_CHOICES, default='Buyer')
	address 					= models.TextField(max_length=120)
	phone_regex 				= RegexValidator(regex=r'^\+\d{8,17}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number				= models.CharField(validators=[phone_regex], max_length=17, blank=True)
	phone_code					= models.CharField(max_length=6, null=True, blank=True)
	phone_verify				= models.BooleanField(default=False)
	profile_image				= ResizedImageField( upload_to='accounts/images/', null=True, blank=True)
	date_joined					= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login					= models.DateTimeField(verbose_name='last login', auto_now_add=True)
	is_admin					= models.BooleanField(default=False)
	is_active					= models.BooleanField(default=False)
	is_staff					= models.BooleanField(default=False)
	is_superuser				= models.BooleanField(default=False)

	objects = MyAccountManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'address', 'status', 'phone_number']


	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True
