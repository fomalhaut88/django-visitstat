from django.contrib import admin

from visitstat import models


class VisitAdmin(admin.ModelAdmin):
    list_display = ('ip', 'datetime', 'method', 'url', 'querystring', 'referer', 'status', 'reason', 'country', 'city')
    ordering = ('-datetime',)
    list_filter = ('country', 'city')


admin.site.register(models.Visit, VisitAdmin)
