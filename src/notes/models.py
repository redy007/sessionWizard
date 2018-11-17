from django.db import models

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title

class Rezervace_typy_zivnosti(models.Model):
    jmena_typu = models.CharField(max_length=120)
    jazyk_zivnosti = models.CharField(max_length=3)

class Rezervace_zivnosti(models.Model):
    jmeno_zivnosti = models.CharField(max_length=120)
    jazyk_zivnosti = models.CharField(max_length=3)
    typ_zivnosti = models.ForeignKey(Rezervace_typy_zivnosti, on_delete=models.SET_NULL, null=True)
