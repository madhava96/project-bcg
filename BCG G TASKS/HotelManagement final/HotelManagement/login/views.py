from django.shortcuts import render
from .models import login
from django.contrib import messages

# Create your views here.
user=''

def loginpage(request):
    global user
    
    print(request)
    if request.method == 'GET':
        return render(request,'loginpage.html')
    else: #login authentication
        global username
        username=request.POST.get('username')
        password=request.POST.get('password')
        print('a',username,password)
        uname=login.objects.filter(username=username)
        pwd=login.objects.filter(password=password)
        print('b:',uname,pwd)
        if uname and pwd:
            dsig = login.objects.filter(username=username)
            for i in dsig:
                dsg=i.designation 
                if dsg =='Manager':
                    user='Manager'
                    #return render(request,'Managerhomepage.html') 
                    return render(request,'user.html',{'d':'Manager'})
                elif dsg =='Admin':
                    user='Admin'
                    #return render(request,'Adminhomepage.html')
                    return render(request,'user.html',{'d':'Admin'})
                elif dsg=='Receptionist':
                    user='Receptionist'
                    #return render(request,'Receptionisthomepage.html')
                    return render(request,'user.html',{'d':'Receptionist'})
        else:
            return render(request,'loginpage.html')
        
def user(request):
    if user =='Manager':
        return render(request,'user.html',{'d':'Manager'})
    elif user == 'Admin':
        return render(request,'user.html',{'d':'Admin'})
    elif user=='Receptionist':
        return render(request,'user.html',{'d':'Receptionist'})
    else:
        return render(request,'user.html',{'d':'none'})
