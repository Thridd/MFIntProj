from django.db import models
from django.contrib.auth.models import User
import uuid
import json, os, sys
# Create your models here.

#Model for the comments stored in the DB
class Comment(models.Model):
    commentID = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    articleID = models.UUIDField(primary_key=False, default=uuid.uuid4(), editable=False)
    text = models.CharField(max_length=10000)
    date_posted = models.DateTimeField(auto_now_add=True)
