# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cars(models.Model):
    brand = models.CharField(primary_key=True, max_length=100)
    type = models.CharField(max_length=100)
    cm3 = models.IntegerField()
    power = models.IntegerField()
    carburant = models.CharField(max_length=100)
    min_emission_co2 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    max_emission_co2 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    min_consumation = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    max_consumation = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars'
        unique_together = (('brand', 'type', 'cm3', 'power', 'carburant'),)
