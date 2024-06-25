from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Branch(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
