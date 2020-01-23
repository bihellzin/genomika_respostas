from django.db import models


class Doencas(models.Model):
    doenca = models.CharField(max_length=150)
    gene = models.CharField(max_length=20)

    def __str__(self):
        return self.doenca


class Usuarios(models.Model):
    username = models.CharField(max_length=20, unique=True, primary_key=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
