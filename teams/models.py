from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=200)
    logo = models.CharField(max_length=200, default="https://www.tresmonjitas.com/wp-content/uploads/2018/07/PlaceholderLogo.png")
    
    def __str__(self):
        return self.name