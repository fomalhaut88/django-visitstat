from datetime import timedelta

from django.db import models
from django.utils import timezone


class Visit(models.Model):
    datetime = models.DateTimeField()
    ip = models.CharField(max_length=15)
    method = models.CharField(max_length=6)
    url = models.CharField(max_length=1000)
    referer = models.CharField(max_length=1000, null=True, blank=True, default=None)
    querystring = models.TextField(null=True, blank=True, default=None)
    status = models.IntegerField()
    reason = models.CharField(max_length=64)
    country = models.CharField(max_length=100, null=True, default=None, blank=True)
    city = models.CharField(max_length=100, null=True, default=None, blank=True)

    def __unicode__(self):
        return self.ip

    @classmethod
    def get_views_today(cls):
        t_from = timezone.now().replace(hour=0, minute=0, second=0)
        return cls.objects.filter(datetime__gte=t_from).count()

    @classmethod
    def get_visitors_24(cls):
        now = timezone.now()
        t_from = timezone.now() - timedelta(days=1)
        return cls.objects.filter(datetime__gte=t_from). \
            aggregate(models.Count('ip', distinct=True))['ip__count']

    @classmethod
    def get_visitors_today(cls):
        t_from = timezone.now().replace(hour=0, minute=0, second=0)
        return cls.objects.filter(datetime__gte=t_from). \
            aggregate(models.Count('ip', distinct=True))['ip__count']
