from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['start_date']

class Project(models.Model):
    name = models.CharField(max_length=120)
    tasks = models.ManyToManyField(Task)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']