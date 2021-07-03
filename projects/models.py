import images
from django.db import models
import datetime

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=60)
    desc = models.TextField()
    pub_date = models.DateTimeField(auto_now_add = True)
    project_image1 = models.ImageField(upload_to = 'projects/',default='SOME IMAGE') 
    project_image2 = models.ImageField(upload_to = 'projects/',default='SOME IMAGE')
    project_image3 = models.ImageField(upload_to = 'projects/',default='SOME IMAGE')
    tags = models.ManyToManyField(tags)
    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()
        
    @classmethod
    def all_projects(cls):
        all_projects = cls.objects.order_by('pub_date')
        return all_projects

    @classmethod
    def search_project(cls,search_term):
        project = cls.objects.filter(tags__name__icontains=search_term)
        return project


class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    
    def save_tag(self):
        self.save()
        
# class Categories(models.Model):
