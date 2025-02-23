from django.db import models
import uuid
class Todo(models.Model):
    id= models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    completed= models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title
