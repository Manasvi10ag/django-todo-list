from django.db import models
from django.contrib.auth.models import User  # type: ignore # thats how django handles users & authentication
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # this is a foreign key to the User model, null=True so that the field could be empty
    title = models.CharField(max_length=200) 
    description = models.TextField( null=True, blank=True) 
    complete = models.BooleanField(default=False) 
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete'] # this will order the tasks by complete status