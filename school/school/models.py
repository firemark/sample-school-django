from django.db import models
from os import path

import csv


def load_types(filename):
    dirpath = path.dirname(__file__)
    realpath = path.join(dirpath, filename)
    with open(realpath) as f:
        reader = csv.reader(f)
        return [(int(code), name) for code, name in reader] 


class City(models.Model):
    name = models.CharField(max_length=100)
    coutry_code = models.IntegerField(db_index=True)
    district_code = models.IntegerField(db_index=True)
    comm_code = models.IntegerField(db_index=True)

    def __unicode__(self):
        return self.name


class School(models.Model):
    SCHOOL_CODES = load_types('school_codes.csv')
    school_code = models.IntegerField(db_index=True, choices=SCHOOL_CODES)
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, db_index=True)
    street = models.CharField(max_length=100)
    street_nr = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=10)
    patron = models.CharField(max_length=150, blank=True, null=True)
    site = models.CharField(max_length=200, blank=True, null=True)
    telephone = models.CharField(max_length=30, null=True, blank=True)
    boys = models.IntegerField(default=0)
    girls = models.IntegerField(default=0)
    agencies = models.IntegerField(default=0)
    fulltime_teachers = models.IntegerField(default=0)
    nonfulltime_teachers = models.IntegerField(default=0)

