from django.db import models
from os import path

import csv


def load_types(filename):
    dirpath = path.basename(__file__)
    realpath = path.join(dirpath, filename)
    with open(realpath) as f:
        reader = csv.reader(f)
        return [(int(code), name) for code, name in reader] 


class City(models.Model):
    name = models.CharField(max_length=100)
    coutry_code = models.IntegerField(db_index=True)
    disctrict_code = models.IntegerField(db_index=True)
    comm_code = models.IntegerField(db_index=True)


class School(models.Model):
    SCHOOL_CODES = load_types('school_codes.csv')
    school_code = models.IntegerField(db_index=True, choices=CODES)
    city = models.ForeignKey(City, db_index=True)
    street = models.CharField(max_length=100)
    street_nr = models.IntegerField()
    zip_code = models.CharField(max_length=10)
    patron = models.CharField(max_length=150, blank=True, null=True)
    boys = models.IntegerField(default=0)
    girls = models.IntegerField(default=0)
    agencies = models.IntegerField(default=0)
    fulltime_teachers = models.IntegerField(default=0)
    nonfulltime_teachers = models.IntegerField(default=0)

