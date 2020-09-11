import time
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from carts.models import Cart
from .models import Order
from .utils import id_generator

# Create your views here.

@login_required
def orders(request):

	context = {}
	template = 'orders/user.html'
	return render(request, template, context)


@login_required
def checkout(request):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		the_id = None
		return redirect(reverse('cart'))


	try:
		new_order = Order.objects.get(cart=cart)
	except Order.DoesNotExist:
		new_order = Order()
		new_order.cart = cart
		new_order.user = request.user
		new_order.order_id = id_generator()
		new_order.save()
	except:
		return redirect(reverse('cart'))

	if new_order.status == 'Finished':
		# cart.delete()
		del request.session['cart_id']
		del request.session['items_total']
		return redirect(reverse('cart'))

	context = {}
	template = 'products/home.html'
	return render(request, template, context)