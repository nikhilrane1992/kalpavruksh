from django.core.exceptions import ObjectDoesNotExist
from models import *
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, JsonResponse
from datetime import datetime, timedelta

class KalpavrukshMiddleware(object):
    def process_request(self, request):
        params = request.GET
        if params.get('api_key'):
            try:
                tenent = Tenant.objects.get(api_key=params.get('api_key'))
                if tenent.next_request_timestamp + timedelta(seconds=10) < datetime.now():
                    tenent.api_request_count += 1
                    tenent.next_request_timestamp = datetime.now()
                    tenent.save()
                else:
                    return JsonResponse({
                        "message": "Try After 10 Seconds", 
                        "status": False,
                    })
            except ObjectDoesNotExist:
                return JsonResponse({
                    "message": "Invalid Api Key", 
                    "status": False,
                })