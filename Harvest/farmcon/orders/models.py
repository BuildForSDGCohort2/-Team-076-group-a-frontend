from django.contrib.auth import get_user_model
from django.db import models
import time

# Create your models here.
# from carts.models import Carts

User = get_user_model()


STATUS_CHOICES = (
				('Started', 'Started'),
				('Abandoned', 'Abandoned'),
				('Finshed', 'Finshed'),
				)


class Order(models.Model):
	user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
	order_id = models.CharField(max_length=120, default=str(time.time()), unique=True)
	# cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	status = models.CharField(max_length=120, choices=STATUS_CHOICES, default='Started')

	sub_total = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
	tax = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
	final_total = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.order_id