from django.db import models

# Create your models here.


class Usuario(models.Model):
    #SEXO_CHOICES = [         ["F", "Feminino"],         ["M", "Masculino"],        ["N", "Nenhuma das opções"]    ]

    nome = models.CharField(max_length=50)
#    email = models.EmailField(null=False)
#