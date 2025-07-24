from django.utils.text import slugify
from django.db import models


class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating}⭐"


# models.py




class Job(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    location = models.CharField(max_length=100, default="India")
    job_type = models.CharField(max_length=50, default="Full time")
    stipend = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    applied_at = models.DateTimeField(auto_now_add=True)  
