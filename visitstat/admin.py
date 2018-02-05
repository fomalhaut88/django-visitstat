from django.contrib import admin

from visitstat import models


class VisitAdmin(admin.ModelAdmin):
    list_display = ('ip', 'datetime', 'method', 'url', 'querystring', 'referer', 'status', 'reason')
    ordering = ('-datetime',)


admin.site.register(models.Visit, VisitAdmin)
