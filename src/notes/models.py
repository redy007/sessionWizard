from django.db import models
from django.contrib.auth.models import Group

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

    def __str__(self):
        return self.jmeno_zivnosti

class Zivnosti(models.Model):
    jmeno_zivnosti = models.ForeignKey(Rezervace_zivnosti, on_delete=models.CASCADE, null=True)
    typ_zivnosti = models.ForeignKey(Rezervace_typy_zivnosti, on_delete=models.CASCADE, null=True)
    jazyk_zivnosti = models.CharField(max_length=3)

# do provozniDoby a firmy budes zapisovat data, proto je tam take mas
class ProvozniDoba(models.Model):
    """docFtring for ProvozniDoba"""
    den = models.IntegerField( blank=True)
    otevreno_od = models.TimeField(blank=True,null=True)
    otevreno_do = models.TimeField(blank=True, null=True)
    otevreno = models.CharField(max_length=1, default="T")
    firma = models.ForeignKey(Group, related_name='fdoba', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('den', 'firma'),)

class Firma(models.Model):
    """docFtring for firma"""
    firma = models.ForeignKey(Group, related_name='ffirma', on_delete=models.CASCADE)
    jmeno_firmy = models.CharField(max_length=100)
    adresa = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, default="+420")
    url = models.CharField(max_length=100)
    geo = models.CharField(max_length=100, blank=True, null=True)
    mena = models.CharField(max_length=3)
    kalendar = models.CharField(max_length=1, default="P")
    jazyk = models.CharField(max_length=15)
    widget = models.CharField(max_length=20) # odkaz na widget na disku
    template = models.IntegerField(default=1) # barvy
