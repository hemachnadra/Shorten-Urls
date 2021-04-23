from django.db import models

# Create your models here.

class Url(models.Model):
    slug=models.SlugField(unique=True)
    url=models.TextField(null=False)
    #new_url=models.TextField(null=True)

    def __str__(self):
        return f'Short URL for :{self.url} is {self.slug}'

    