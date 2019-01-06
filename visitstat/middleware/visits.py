from django.utils import timezone

from visitstat.models import Visit


class StatisticsMiddleware(object):
    def process_response(self, request, response):
        try:
            Visit.objects.create(
                datetime=timezone.now(),
                ip=request.META.get('REMOTE_ADDR'),
                method=request.method,
                url=request.path,
                referer=request.META.get('HTTP_REFERER'),
                querystring=self._get_querystring(request),
                status=response.status_code,
                reason=response.reason_phrase
            )
        except:
            pass
        return response

    def _get_querystring(self, request):
        if request.method in ['GET', 'POST']:
            return getattr(request, request.method).urlencode()
        else:
            return None
