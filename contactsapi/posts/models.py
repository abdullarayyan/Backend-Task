from django.db import models
from django.contrib.auth.models import User

# Create your mo

class Posts(models.Model):
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    user_id = models.IntegerField(null=False, blank=False, default="-1",primary_key=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
