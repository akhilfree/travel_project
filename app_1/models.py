from django.db import models

# Create your models here.

class place(models.Model):
    place = models.CharField(max_length=30)
    desc = models.CharField(max_length=30)
    img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.place

class head_dept(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=30)
    img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

class user_data(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
