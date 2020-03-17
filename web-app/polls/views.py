from django.shortcuts import render
from django.http import HttpResponse
from .models import Activity
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from basicauth.decorators import basic_auth_required
import time


# Create your views here.
def index(request):
    return HttpResponse("Hh")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

@csrf_exempt
def add(request):
    if request.method == 'POST':
#        print(request.body)
        return HttpResponse("Website recieved activity: " + str(request.body))

def list(request):
    #if request.method == 'GET':
    serialized_queryset = serializers.serialize('python', Activity.objects.all())
#    print(serialized_queryset)
    return JsonResponse(serialized_queryset, safe=False)

@csrf_exempt
@basic_auth_required
def activities(request):
    if request.method == 'POST':
        activity_name = request.POST.get("activity_name","")
        activity_description = request.POST.get("activity_description","")
        activity_repetition = request.POST.get("repetition","")
        start = time.time()
        b1 = Activity(name=activity_name, description=activity_description, repetition=activity_repetition)
        b1.save()
        end = time.time()
        print("Time taken to store single object: ", end - start, " seconds")

    istekler = Activity.objects.all()
    
    start = time.time()
    render(request, 'list.html', locals())
    end = time.time()
    print("Time taken to render: ", end - start, " seconds")

    start = time.time()
    test_activity = Activity.objects.get(pk=1)
    end = time.time()
    print("Single object from database: Name: " + test_activity.name + ", Description: " + test_activity.description)
    print("Time taken to get single object from database: ", end - start, " seconds")

    return render(request, 'list.html', locals())
