from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render_to_response, render
from models import *
from django.db.models import Count, Min, Sum, Avg

def index(request):
    return render_to_response('templates/index.html')


def questions(request):
    params = request.GET
    kwargs = {}
    if params.get('id'):
        kwargs['id'] = params.get('id')
    if params.get('title'):
        kwargs['title__icontains'] = params.get('title')
    kwargs['private'] = False
    return JsonResponse({
        "data": [{
            "title": que.title,
            "id": que.id,
            "answers": [{
                "answer": ans.body,
                "user": ans.user.name,
                "id": ans.id
            } for ans in que.answer_set.all()]
        } for que in Question.objects.filter(**kwargs)], 
        "status": True,
    })


def dashboard_summary(request):
    tot_que = Question.objects.all().count()
    tot_ans = Answer.objects.all().count()
    tot_users = User.objects.all().count()

    return JsonResponse({
        "tot_que": tot_que,
        "tot_ans": tot_ans,
        "tot_users": tot_users,
        "tenent_api_counts": [{
            "count":  TenantAPICount.objects.filter(tenant=tenant).aggregate(Sum('api_request_count'))['api_request_count__sum'],
            "name": tenant.name,
            "api_key": tenant.api_key
        } for tenant in Tenant.objects.all()],
        "status": True,
    })