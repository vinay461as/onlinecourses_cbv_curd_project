from django.db import models
from django.urls import reverse

# Create your models here.
# web development, React, Angular, Node.Js, WordPress, JavaScript, Css, php, python, Django

class Courses(models.Model):
    COURSE_CHOICES = (
        ('All Levels', 'All Levels'),
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Expert', 'Expert'),
    )

    title = models.CharField(max_length=250)
    description = models.TextField()
    provided_by = models.CharField(max_length=100)
    lectures = models.IntegerField()
    hours = models.IntegerField()
    type = models.CharField(max_length=20, choices=COURSE_CHOICES)
    price = models.FloatField()
    updated = models.DateField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('courses')
