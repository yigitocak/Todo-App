from django.db import models


class Task(models.Model):
    task_name = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default='open')

    def __str__(self):
        return self.task_name
