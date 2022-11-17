from django.db import models

# Create your models here.
class Usuario(models.Model):
    login = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True)
    
    def __str__(self):
        return self.login
    