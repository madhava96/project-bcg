from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages

from .models import login,empdata,stockdata
from django.http import HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


# Create your views here.


def userhomepage(request):
    return render(request,"userhomepage.html") #display user home page


def managerhomepage(request):
    return render(request,'managerhomepage.html') #display manager home  page



def loginpage(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else: #login authentication
        global username
        username=request.POST.get('username')
        password=request.POST.get('password')
        uname=login.objects.filter(username=username)
        pwd=login.objects.filter(password=password)

        if uname and pwd:
            dsig = login.objects.filter(username=username)
            for i in dsig:
                dsg=i.designation
                if dsg =='SE':
                    return render(request,'managerhomepage.html')
               
                else:
                   
                    return render(request,'userhomepage.html')
        else:
            messages.success(request,'Invalid details!')
            return render(request,'login.html')
             #return HttpResponse("error")
             
           
       


def employeeform(request):
   
    if request.method=='GET':
        empdat=empdata.objects.all().values()  #displaying the values that are before saved
         
        return render(request,'employeeform.html',{'empdat':empdat})
         
   
    elif request.method=='POST':
         empid=request.POST['eid']
         if empdata.objects.filter(empid=empid).exists(): # it checks id is already registered or not
            messages.error(request,"Employee ID already registered !")  
            return render(request,'employeeform.html')

         else :
            empdata(                                
                empid=request.POST.get('eid'),
                enum=request.POST.get('enum'),
                empname=request.POST.get('empname'),
                designation=request.POST.get('designation'),
                specialization=request.POST.get('specialization'),
                doj=request.POST.get('doj'),
                expsalary=request.POST.get('esal'),
                prevexp=request.POST.get('prevexp'),
           
           
            ).save()  #saving all the form data in models
       
       
       
           
            messages.success(request,'Form Submitted Successfully') #displaying the form submitting message
            empdat=empdata.objects.all().values() #displaying the values  after saving
       
            return render(request,'employeeform.html',{'empdat':empdat})

def employeemanagerform(request):
   
    if request.method=='GET':
        empdat=empdata.objects.all().values()  #displaying the values that are before saved
         
        return render(request,'empmanager.html',{'empdat':empdat})
         
   
    elif request.method=='POST':
         empid=request.POST['eid']
         if empdata.objects.filter(empid=empid).exists():   # it checks id is already registered or not
            messages.error(request,"Employee ID already registered !")
            return render(request,'empmanager.html')

         else :
            empdata(
                empid=request.POST.get('eid'),
                enum=request.POST.get('enum'),
                empname=request.POST.get('empname'),
                designation=request.POST.get('designation'),
                specialization=request.POST.get('specialization'),
                doj=request.POST.get('doj'),
                expsalary=request.POST.get('esal'),
                prevexp=request.POST.get('prevexp'),
           
           
            ).save()  #saving all the form data in models
       
       
       
           
            messages.success(request,'Form Submitted Successfully') #displaying the form submitting message
            empdat=empdata.objects.all().values() #displaying the values  after saving
       
            return render(request,'empmanager.html',{'empdat':empdat})

       
def stockform(request):
    if request.method=='GET':
        stockdat=stockdata.objects.all().values()  #displaying the values that are before saved
        return render(request,'stockform.html',{'stockdat':stockdat})  
    else:
        stockdata(
            medicine=request.POST.get('medicine'),
            quantity=request.POST.get('quantity'),
            price=request.POST.get('price'),
             
        ).save()  #saving all the form data in models
        messages.success(request,'Form Submitted Successfully') #displaying the form submitting message
        stockdat=stockdata.objects.all().values() #displaying the values  after saving
        return render(request,'stockform.html',{'stockdat':stockdat})


def stockmanagerform(request):
    if request.method=='GET':
        stockdat=stockdata.objects.all().values()  #displaying the values that are before saved
        return render(request,'stockmanager.html',{'stockdat':stockdat})  
    else:
        stockdata(
            medicine=request.POST.get('medicine'),
            quantity=request.POST.get('quantity'),
            price=request.POST.get('price'),
           
        ).save()  #saving all the form data in models
        messages.success(request,'Form Submitted Successfully') #displaying the form submitting message
        stockdat=stockdata.objects.all().values() #displaying the values  after saving
        return render(request,'stockmanager.html',{'stockdat':stockdat})

def logoutpage(request):
   
    return redirect('loginpage')


def employeedata(request):
    if request.method=='GET':
        empdat = empdata.objects.all()
        page = request.GET.get('page', 1)  #pagination
        paginator = Paginator(empdat, 5)  #displaying 5 rows in a page
        try:
            empdat = paginator.page(page)
        except PageNotAnInteger:
            empdat = paginator.page(1) #if the page is not integer it will be 1
        except EmptyPage:
            empdat = paginator.page(paginator.num_pages)
       
        return render(request, 'employeedata.html', { 'empdat': empdat })
    else:
        empdata(
            empid=request.POST.get('eid'),
            enum=request.POST.get('enum'),
            empname=request.POST.get('empname'),
            designation=request.POST.get('designation'),
            specialization=request.POST.get('specialization'),
            doj=request.POST.get('doj'),
            expsalary=request.POST.get('esal'),
            prevexp=request.POST.get('prevexp'),
            ).save()  #saving all the form data in models
        empdat=empdata.objects.all().values() #displaying the values  saved
       
        return render(request,'employeedata.html',{'empdat':empdat})


def stockformdata(request):
    if request.method=='GET':
        stockdat = stockdata.objects.all()
        page = request.GET.get('page', 1)  #pagination
        paginator = Paginator(stockdat, 5)  #displaying 5 rows in a page
        try:
            stockdat = paginator.page(page)
        except PageNotAnInteger:
            stockdat = paginator.page(1) #if the page is not integer it will be 1
        except EmptyPage:
            stockdat = paginator.page(paginator.num_pages)
       
        return render(request, 'stockdata.html', { 'stockdat': stockdat })

    else:
        stockdata(
            medicine=request.POST.get('medicine'),
            quantity=request.POST.get('quantity'),
            price=request.POST.get('price'),
            ).save()  #saving all the form data in models
        stockdat=stockdata.objects.all().values() #displaying the values  saved
       
        return render(request,'stockdata.html',{'stockdat':stockdat})


