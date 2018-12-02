from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title

class Rezervace_typy_zivnosti(models.Model):
    jmena_typu = models.CharField(max_length=120)

    def __str__(self):
        return self.jmena_typu

class Rezervace_zivnosti(models.Model):
    jmeno_zivnosti = models.CharField(max_length=120)
    typ_zivnosti = models.ForeignKey(Rezervace_typy_zivnosti, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.jmeno_zivnosti

class Zivnosti(models.Model):
    jmeno_zivnosti = models.ForeignKey(Rezervace_zivnosti, on_delete=models.CASCADE, null=True)
    typ_zivnosti = models.ForeignKey(Rezervace_typy_zivnosti, on_delete=models.CASCADE, null=True)
    jazyk_zivnosti = models.CharField(max_length=3)

class Contact(models.Model):
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    web_page = models.CharField(max_length=100)

class Settings(models.Model):
    currency = models.CharField(max_length=20)
    # nastaveni kalendare (zacatek v pondeli nebo nedeli)


class Firma(models.Model):
    jmeno_firmy = models.CharField(max_length=100)
    login = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    zivnost = models.ForeignKey(Zivnosti, on_delete=models.CASCADE)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    settings = models.OneToOneField(Settings, on_delete=models.CASCADE)


