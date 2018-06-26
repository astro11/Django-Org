from django.db import models
from uuid import uuid4

# Create your models here.
class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)    
    title = models.CharField(max_length=200)    
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return '%s %s' % (self.title, self.id)