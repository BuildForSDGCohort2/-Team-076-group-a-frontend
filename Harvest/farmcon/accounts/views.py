from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


from .models import UserAccount
from .forms import LoginForm, RegistrationForm, VerifyNumber, AccountUpdate
from twilio.rest import Client
import string, random, time
# Create your views here.


def logout_view(request):
	logout(request)
	return redirect('home')


def login_view(request):
	context = {}
	if request.user.is_authenticated:
		if request.user.status == 'Farmer':
			return redirect('farmer')
		else:
			return redirect('buyer')
	if request.POST:
		form = LoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user = authenticate(email=email, password=password)
			login(request, user)
			# print(user.status)
			# return redirect('home')
			if user.status == 'Farmer':
				return redirect('farmer')
			else:
				return redirect('buyer')
		else:
			context['form'] = form
	else:
		form = LoginForm()
		context['form'] = form

	template = 'account/login.html'
	return render(request, template, context)



def register_view(request):
	context = {}
	if request.user.is_authenticated:
		if request.user.status == 'Farmer':
			return redirect('farmer')
		else:
			return redirect('buyer')

	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()

			current_site = get_current_site(request)
			mail_subject = 'Activate your Farmcon Account.'
			message = render_to_string('account/send_email.html', {
				'user': form,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user)
				})
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(mail_subject, message, to=[to_email])
			email.send()

			return redirect('email_sent')
		else:
			context['form'] = form
	else:
		form = RegistrationForm()
		context['form'] = form

	template = 'account/register.html'
	return render(request, template, context)


def email_sent(request):
	context = {}
	template = 'account/email_sent.html'
	return render(request, template, context)


def activate_email(request, uidb64, token):
	context = {}
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = UserAccount.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, UserAccount.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		context['message'] = 'You can now login into your account'
	else:
		context['message'] = 'Activation link is invalid'

	template = 'account/activate_email.html'
	return render(request, template, context)



@login_required
def update_profile(request):

	if not request.user.is_authenticated:
		return redirect('login')

	context = {}

	if request.POST:
		form = AccountUpdate(request.POST, request.FILES or None, instance=request.user)
		if form.is_valid():
			form.save()
			if request.user.status == 'Farmer':
				return redirect('farmer')
			else:
				return redirect('buyer')
	else:
		form = AccountUpdate(initial = {
				"email": request.user.email,
				'username': request.user.username,
				'first_name': request.user.first_name,
				'last_name': request.user.last_name,
				'address': request.user.address,
				'phone_number': request.user.phone_number,
				'profile_image': request.user.profile_image
			}
		)
	template = 'account/update.html'
	context['form'] = form
	return render(request, template, context)



@login_required
def farmer_view(request):
	context = {}

	if request.user.status == 'Buyer':
		return redirect('buyer')


	template = 'general/farmer.html'
	return render(request, template, context)


@login_required
def buyer_view(request):
	context = {}

	if request.user.status == 'Farmer':
		return redirect('farmer')



	template = 'general/buyer.html'
	return render(request, template, context)




# @login_required
def verify_number(request):
	context = {}
	code_to_send = request.session['code']
	# if request.method == 'POST':
	form = VerifyNumber(request.POST, instance=request.user)
	if form.is_valid():
		user_entry = form.cleaned_data['phone_code']
		if user_entry != code_to_send:
			print('code not correct')
			# return redirect('verify_number')
		else:
			user = form.save(commit=False)
			user.phone_verify = True
			user.save()
			del request.session['code']
			if request.user.status == 'Farmer':
				return redirect('farmer')
			else:
				return redirect('buyer')


	context['response'] = 'Message sent'
	context['form'] = form
	template = 'account/verify_number.html'
	return render(request, template, context)


@login_required
def send_code(request):
	context = {}
	if request.user.phone_verify:
		if request.user.status == 'Farmer':
			return redirect('farmer')
		else:
			return redirect('buyer')
	chars = string.ascii_uppercase + string.digits
	code_to_send = ''.join(random.choice(chars) for _ in range(6))
	request.session['code'] = code_to_send
	client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
	send_from  = settings.TWILIO_SEND_FROM
	# send_to = settings.TWILIO_SEND_TO
	send_to = request.user.phone_number
	client.messages.create(to=send_to, from_=send_from, body=code_to_send)

	return redirect('verify_number')



@login_required
def user_profile(request):
	if not request.user.is_authenticated:
		return redirect('login')

	user = request.user
	context = {}
	context['username'] = user.username
	context['email'] = user.email
	context['first_name'] = user.first_name
	context['last_name'] = user.last_name
	context['phone_number'] = user.phone_number
	context['address'] = user.address
	context['profile_image'] = user.profile_image
	context['status'] = user.status
	context['date_joined'] = user.date_joined

	template = 'account/profile.html'
	return render(request, template, context)