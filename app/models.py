from django.db import models


class Task(models.Model):
    task = models.CharField(max_length=200)
    taskId = models.CharField(max_length=200)

    class Meta:
        ordering = ['taskId']
    
    def __str__(self):
        return self.task