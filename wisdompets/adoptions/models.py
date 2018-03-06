from django.db import models

class Pet(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=150)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)

    # blank=True means the field is optional
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()

    # null=True instead of blank=True because blank integer field results in value of zero
    # which is not distinguishable from the case when the pet is less than one year old
    age = models.IntegerField(null=True)

    # blank=True because some pets might have zero vaccinations
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
