from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=64, verbose_name='Title')
