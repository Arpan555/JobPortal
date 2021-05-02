from django.shortcuts import render
from jobapp.models import *

# Create your views here.
def index(request):
     return render(request,'jobapp/index.html')
def indorejob(request):
     job_list=Indorejob.objects.order_by('date')
     my_dict={'job_list':job_list}
     return render(request,'jobapp/indorejob.html',context=my_dict)
def punejob(request):
     job_list=Punejob.objects.order_by('date')
     my_dict={'job_list':job_list}
     return render(request,'jobapp/punejob.html',context=my_dict)
def banglorejob(request):
     job_list=Banglorejob.objects.order_by('date')
     my_dict={'job_list':job_list}
     return render(request,'jobapp/banglore.html',context=my_dict)
def hyderabadjob(request):
     job_list=Hyderabadjob.objects.order_by('date')
     my_dict={'job_list':job_list}
     return render(request,'jobapp/hyderabad.html',context=my_dict)


