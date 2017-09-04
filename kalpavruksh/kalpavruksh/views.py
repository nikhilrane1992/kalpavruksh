from uuid import uuid4

from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render_to_response, render
from models import Question

def index(request):
    return render_to_response('templates/index.html')


def questions(request):
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
    	"api_key": str(uuid4()), 
    	"status": True,
    })