from django.db import models
from django.shortcuts import render,redirect

class info(models.Model):
    name=models.CharField(max_length=200,default='')
    information = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='store/info', default='')

    def __str__(self):
        return self.name
    @staticmethod
    def info_get_all():
        return info.objects.all()


