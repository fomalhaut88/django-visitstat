import os

import geoip2.database
import geoip2.errors

from django.db.transaction import atomic

from visitstat import models


ROOT_DIR = os.path.dirname(__file__)
LIMIT = 1000


@atomic
def visit_geoip_fill():
    visits = models.Visit.objects.filter(country__isnull=True)[:LIMIT]

    if visits:
        mmdb_path = os.path.join(ROOT_DIR, 'data/GeoLite2-City.mmdb')
        reader = geoip2.database.Reader(mmdb_path)

        for visit in visits:
            try:
                response = reader.city(visit.ip)
                visit.country = response.country.name
                visit.city = response.city.name
            except geoip2.errors.AddressNotFoundError:
                visit.country = "-"
                visit.city = "-"
            visit.save()
