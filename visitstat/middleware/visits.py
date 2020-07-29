import logging
from django.utils import timezone

from visitstat.models import Visit


class StatisticsMiddleware(object):
    def process_response(self, request, response):
        ip = request.META.get('HTTP_X_FORWARDED_FOR') or \
             request.META.get('HTTP_X_REAL_IP') or \
             request.META.get('REMOTE_ADDR')
        try:
            Visit.objects.create(
                datetime=timezone.now(),
                ip=ip,
                method=request.method,
                url=request.path,
                referer=request.META.get('HTTP_REFERER'),
                querystring=self._get_querystring(request),
                status=response.status_code,
                reason=response.reason_phrase
            )
        except Exception as exc:
            logging.error(exc)
        return response

    def _get_querystring(self, request):
        if request.method in ['GET', 'POST']:
            return getattr(request, request.method).urlencode()
        else:
            return None
