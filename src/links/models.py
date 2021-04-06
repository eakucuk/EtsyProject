from django.db import models
from .utils import get_link_data
from .forms import AddLinkForm


# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length=500, blank=True)
    price = models.CharField(max_length=20, blank=True)
    image = models.CharField(max_length=1000, blank=True)






