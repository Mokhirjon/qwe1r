from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .models import Subjects

def get_by_index(request):
    if request.method=='GET':
        data={'data':'This data'}
        return JsonResponse (data=data)

def get_all(request):
    if request.method=='GET':
        all_data= Subjects.objects.all()
        result=[]
        for subject in all_data:
            result.append({'id':subject.id,
                           'subject_name':subject.subjects_name})
    return JsonResponse({'data':result})