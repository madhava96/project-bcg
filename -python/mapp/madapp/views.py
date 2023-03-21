from django.shortcuts import render
from .models import empdtls
# Create your views here.
def empdata(request):
    return render(request,'madapp/employees.html')
