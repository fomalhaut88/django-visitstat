import pytz
from datetime import datetime

from visitstat.models import Visit



class StatisticsMiddleware(object):
    def process_response(self, request, response):
        visit = Visit(
            datetime=datetime.now(pytz.utc),
            ip=request.META.get('REMOTE_ADDR'),
            method=request.method,
            url=request.path,
            referer=request.META.get('HTTP_REFERER'),
            querystring=getattr(request, request.method).urlencode(),
            status=response.status_code,
            reason=response.reason_phrase
        )
        visit.save()
        return response
