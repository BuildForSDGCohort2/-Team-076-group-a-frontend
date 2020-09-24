from django.db import models


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

    def indexing(self):
        from productsearch.documents import ProductDocument
        obj = ProductDocument(
            meta={'id': self.id}, title=self.title, description=self.description, price=self.price
        )
        obj.save()
        return obj.to_dict(include_meta=True)
