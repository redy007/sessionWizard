from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title

class BusinessCategories(models.Model):
    business_category = models.CharField(max_length=120)

    def __str__(self):
        return self.business_category

class BusinessTypes(models.Model):
    business_name = models.CharField(max_length=120)
    business_category = models.ManyToManyField(BusinessCategories, through='Business')

    def __str__(self):
        return self.business_name

class Business(models.Model):
    business_name = models.ForeignKey(BusinessTypes, on_delete=models.CASCADE, null=True)
    business_category = models.ForeignKey(BusinessCategories, on_delete=models.CASCADE, null=True)
    language = models.CharField(max_length=3)

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    login = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    company_uuid = models.UUIDField(null=True, blank=True,)

class Contact(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    url = models.CharField(max_length=100)

class OpenHours(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    day = models.IntegerField(blank=True)
    open_from = models.TimeField(blank=True, null=True)
    closed_at = models.TimeField(blank=True, null=True)
    pause_starts = models.TimeField(blank=True, null=True)
    pause_finish = models.TimeField(blank=True, null=True)
    is_open = models.CharField(max_length=1, default="T")

    class Meta:
        unique_together = (('day', 'company'),)
