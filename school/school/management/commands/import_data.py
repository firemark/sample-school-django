from django.core.management import BaseCommand
from django.db import transaction
from school.models import City, School

import csv
import sys


class Command(BaseCommand):
    help = "elo"

    def add_arguments(self, parser):
        parser.add_argument('filename')

    def handle(self, *args, **kwargs):
        with transaction.atomic(), open(kwargs['filename']) as f:
            reader = csv.reader(f)
            try:
                for line, data in enumerate(reader, start=1):
                    self.import_data(data)
            except:
                sys.stderr.write('Error on line: %d:\n' % line)
                raise

    def get_city(self, data):
        return City.objects.get_or_create(
            coutry_code=data[0],
            district_code=data[1],
            comm_code=data[2],
            name=data[3],
        )[0]

    def import_data(self, data):
        all_students = int(data[-7])
        girls = int(data[-6])
        School.objects.create(
            city=self.get_city(data[1:5]),
            school_code=int(data[6]),
            name=data[8],
            patron=data[9],
            street=data[10],
            street_nr=data[11],
            zip_code=data[12],
            telephone=data[14],
            site=data[16],
            boys=all_students-girls,
            girls=girls,
            agencies=int(data[-4].partition(',')[0]),
            fulltime_teachers=data[-3],
            nonfulltime_teachers=data[-2],
        )

