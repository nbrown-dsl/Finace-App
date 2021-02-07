from django.db import models
from django.utils.text import slugify

"""this is the model for project"""
class Project(models.Model):
    name = models.CharField(max_length=100)#name of the project
    slug = models.SlugField(max_length=100,unique=True, blank=True)
    budget = models.IntegerField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

"""This is the model for expanses"""
class Expanse(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='expanses')
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)