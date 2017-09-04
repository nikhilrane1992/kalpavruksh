from django.core.exceptions import ObjectDoesNotExist
from models import *
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, JsonResponse
from datetime import datetime, timedelta

class KalpavrukshMiddleware(object):
    def process_request(self, request):
        params = request.GET
        if params.get('api_key'):
            current_date = datetime.now()
            try:
                tenant = Tenant.objects.get(api_key=params.get('api_key'))
                tenant_api_count, created = TenantAPICount.objects.get_or_create(
                    tenant=tenant,
                    created__year=current_date.year, 
                    created__month=current_date.month, 
                    created__day=current_date.day, 
                )
                if tenant_api_count.next_request_timestamp + timedelta(seconds=10) > current_date and tenant_api_count.api_request_count > 100:
                    return JsonResponse({
                        "message": "Try After 10 Seconds", 
                        "status": False,
                    })
                else:
                    tenant_api_count.api_request_count += 1
                    tenant_api_count.next_request_timestamp = current_date
                    tenant_api_count.save()

            except ObjectDoesNotExist:
                return JsonResponse({
                    "message": "Invalid Api Key", 
                    "status": False,
                })