from django.db import models

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=120, null=False, blank=False)
	description = models.TextField()
	price = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
	slug = models.SlugField(unique=True)
	date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
	date_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	quantity = models.IntegerField(default=10)
	in_stock = models.BooleanField(default=True)


	def __str__(self):
		return self.title

	class Meta:
		unique_together = ('title', 'slug')

	def get_price(self):
		return self.price


class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='products/images/')
	featured = models.BooleanField(default=False)
	thumbnail = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	date_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.product.title