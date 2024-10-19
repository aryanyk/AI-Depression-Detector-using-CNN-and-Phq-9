from django.db import models
import uuid

# Create your models here.

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    email = models.EmailField(max_length=100)
    date_of_birth = models.DateField()
    age = models.IntegerField(null=True, blank=True)
    height = models.FloatField()
    Blood_Group = models.CharField(max_length=10, null=True, blank=True)
    weight = models.FloatField()

    def __str__(self):  
        return self.first_name

# models.py
from django.db import models
from django.contrib.auth.models import User

class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phq9_score = models.IntegerField()
    emotions = models.JSONField()  # Store the detected emotions

    def __str__(self):
        return f"{self.user.username} - {self.phq9_score}"
