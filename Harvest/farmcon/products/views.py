from django.shortcuts import render
from products.models import Product

# Create your views here.

def home_view(request):
	products = Product.objects.all()
	context = {'products': products}

	template = 'general/home.html'
	return render(request, template, context)

	
def all(request):
	products = Product.objects.all()
	context = {'products': products}

	template = 'products/single.html'
	return render(request, template, context)


def single_product(request, slug):
	product = Product.objects.get(slug=slug)
	context = {'product': product}
	template = 'products/single.html'
	return render(request, template, context)


def search(request):
	try:
		q = request.GET.get('q')
	except:
		q = None

	if q:
		products = Product.objects.filter(title__icontains=q)
		context = {'query':q, 'products':products}
		template = 'products/results.html'
	else:
		template = 'general/home.html'
		context = {}
	return render(request, template, context)