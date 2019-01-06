=========
Visitstat
=========

A django application allowing you to log all HTTP requests to your website.

Quick stat
----------

1. Add "visitstat" to your INSTALLED_APPS:

    INSTALLED_APPS = [
        ...
        "visitstat",
    ]

2. Add middleware "visitstat.middleware.visits.StatisticsMiddleware":

    MIDDLEWARE_CLASSES = [
        ...
        'visitstat.middleware.visits.StatisticsMiddleware',
    ]

3. Add a new crontab job:

    CRONJOBS = [
        ...
        ('*/5 * * * *', 'visitstat.cron.visit_geoip_fill'),
    ]

4. Run "python manage.py migrate" to create the table.

Example
-------

To access the statistics within your template:

    {% load visitstat_tags %}

    ...

    {% visitstat_views_today %}
    {% visitstat_visitors_24 %}
    {% visitstat_visitors_today %}

To access the statistics within your Python code:

    from visitstat.models import Visit

    ...
    Visit.get_views_today()
    Visit.get_visitors_24()
    Visit.get_visitors_today()
