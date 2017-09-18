from django.db import models
from django.utils import timezone
# Create your models here.
class post(models.Model):
    author=models.ForeignKey('auth.User')
    text=models.TextField()
    creatd_data=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
