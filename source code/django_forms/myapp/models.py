from django.db import models

# Create your models here.
class Snippet(models.Model):
    book_title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    genre=models.CharField(max_length=50)
    price=models.IntegerField()

    def __str__(self):
        return self.book_title
