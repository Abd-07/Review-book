from django.db import models
import datetime
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    review = models.TextField()
    date = models.DateTimeField(default=timezone.now)

# Create your models here.
