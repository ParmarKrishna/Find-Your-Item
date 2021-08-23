from django.db import models

class userDetail(models.Model):
    email=models.EmailField(max_length=254)
    name=models.CharField(max_length=254)
    password=models.CharField(max_length=254)
    def __str__(self):
        return self.name
