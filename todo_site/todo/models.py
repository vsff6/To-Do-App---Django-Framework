from django.db import models

# Create your models here.

from django.utils import timezone
 
 
class Todo(models.Model):
    #create choices for progress
    Progress = (
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )


    title = models.CharField(max_length=100)
    details = models.TextField()
    assigned_to = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    progress = models.CharField(max_length=100, choices=Progress, default='Not Started')
 
    def __str__(self):
        return self.title