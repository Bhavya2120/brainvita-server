from django.db import models

# Create your models here.
class UserScores(models.Model):
    userName=models.CharField(max_length=255)
    score=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)