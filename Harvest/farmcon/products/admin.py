from django.contrib import admin

# Register your models here.
from products.models import Product, ProductImage

class ProductAdmin(admin.ModelAdmin):
	search_fields = ('title', 'description')
	list_display = ('title', 'price', 'in_stock', 'quantity')
	list_filter = ('price', 'in_stock')
	readonly_fields = ('date_created', 'date_updated')

	class Meta:
		model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)