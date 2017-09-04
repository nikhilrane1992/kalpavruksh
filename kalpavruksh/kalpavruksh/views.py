from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render_to_response, render
from models import *
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    return render_to_response('templates/index.html')


def questions(request):
    params = request.GET
    try:
        tenent = Tenant.objects.get(api_key=params.get('api_key'))
        tenent.api_request_count += 1
        tenent.save()
    except ObjectDoesNotExist:
        return JsonResponse({
            "message": "Invalid Api Key", 
            "status": False,
        })
    return JsonResponse({
        "data": [{
            "question": que.title,
            "id": que.id,
            "answers": [{
                "answer": ans.body,
                "user": ans.user.username,
                "id": ans.id
            } for ans in que.answer_set.all()]
        } for que in Question.objects.filter(private=False)], 
        "status": True,
    })