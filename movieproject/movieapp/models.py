from django.db import models


# Create your models here.
class movie_table(models.Model):
    name = models.CharField(max_length=200)
    dis = models.TextField()
    year = models.IntegerField()
    img=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name