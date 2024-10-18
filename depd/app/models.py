from django.db import models
import uuid

# Create your models here.

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    height = models.FloatField()
    weight = models.FloatField()

    def __str__(self):  
        return self.first_name
