from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
from django.urls import reverse


class categ(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return '{}'.format(self.name)



class Movie(models.Model):
    name = models.CharField(max_length=250, unique=True)
    img = models.ImageField(upload_to='images')
    desc = models.TextField()
    category = models.ForeignKey(categ, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

class Comment(models.Model):
    post=models.ForeignKey(Movie,related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s-%s' %(self.post.name,self.name)
