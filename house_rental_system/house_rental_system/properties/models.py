# properties/models.py

from django.db import models
DEFAULT_IMAGE_URL = 'path/to/default/image.jpg'


class Property(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default=True)
    image = models.ImageField(default=DEFAULT_IMAGE_URL)
    landlord_contact = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
