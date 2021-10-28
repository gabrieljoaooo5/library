from django.db import models

# Create your models here.


class Book(models.Model):
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    isbn = models.IntegerField()
    pagesNumber = models.IntegerField()
    title = models.CharField(max_length=50)
    publicationYear = models.IntegerField()
    publisherEmail = models.EmailField()
