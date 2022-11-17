from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    login = models.CharField(max_length=100)
    senha = models.CharField(blank=True, max_length=100)
    data_nascimento = models.DateField(null=True)
    
    def __str__(self):
        return self.login
    
   
   
   
    def senharandom(senha=True):
        return User.objects.make_random_password(length=14, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889") # zvk0hawf8m6394

        user.set_senha(senha)