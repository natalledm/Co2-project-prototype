# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django import forms

class Cars(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    cm3 = models.IntegerField()
    kw = models.IntegerField()
    carburant = models.CharField(max_length=100)
    min_emission_co2 = models.IntegerField()
    max_emission_co2 = models.IntegerField()
    min_consumption = models.DecimalField(max_digits=10, decimal_places=0)
    max_consumption = models.DecimalField(max_digits=10, decimal_places=0)
    #primary_key=True
    class Meta:
        managed = False # true = python can change it; false = imutable.
        db_table = 'cars'
        # unique_together = (('brand', 'type', 'cm3', 'power', 'carburant'),)
    
    def vehicle(self):
        return self.brand + ' ' + self.model + ' ' + str(self.cm3) + ' ' + str(self.kw) + ' ' + self.carburant

    def comsumption(self):
        return self.vehicle() + ' ' + str(self.min_emission_co2) + ' ' + str(self.max_emission_co2) + ' ' + str(self.min_emission_co2) + ' ' + str(self.max_emission_co2) + ' ' + str(self.min_consumption) + ' ' + str(self.max_consumption)

    def __str__(self):
        return self.comsumption()

class BrandForm(forms.Form):
    brand_name = forms.CharField(label='Brand name', max_length=100)

    def __str__(self):
        return self()
