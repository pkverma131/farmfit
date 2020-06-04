from django.db import models

# Create your models here.

UNIT_CHOICES = (
    (1, 'GRAM'),
    (2, 'POUND'),
    (3, 'OUNCE'),
    (4, 'KG'),
    (5, 'TON')
)

STORAGE_TIME_UNIT_CHOICES = (
    (1, 'HOURS'),
    (2, 'DAYS'),
    (3, 'MONTHS')
)


class Crop(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    unit = models.IntegerField(choices=UNIT_CHOICES)
    yield_ph = models.FloatField()
    # region = models.IntegerField() # RegionCropMapping, Regional Name
    maturity_time = models.IntegerField() # Example: 90 Days
    storage_condition = models.IntegerField()
    storage_time_unit = models.IntegerField(choices=STORAGE_TIME_UNIT_CHOICES) # Example: Days
    storage_time = models.IntegerField() # Example: 100
    # crop_season = models.IntegerField() # SeasonCropMapping
    created_by = models.CharField(max_length=50)
    created_at = models.BigIntegerField()
    modified_at = models.BigIntegerField()
