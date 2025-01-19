from django.db import models

# Create your models here.
class Javobgar(models.Model):
    ismi = models.CharField(max_length=20,null=False, blank=False )
    familiya = models.CharField(max_length=20)
    email = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.ismi

class Topshiriq_turi(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False, unique=True)
    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False, unique=True)
    def __str__(self):
        return self.name


class Task(models.Model):
    mavzu = models.CharField(max_length=120)
    nomer = models.CharField(max_length=25)
    sana = models.DateField(auto_created=True)
    muddat = models.DateField()
    javobgar= models.ForeignKey(Javobgar, on_delete=models.CASCADE)
    topshiriq_turi = models.ForeignKey(Topshiriq_turi, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    natijasi = models.CharField(max_length=300)


    