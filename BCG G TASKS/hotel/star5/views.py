from django.shortcuts import render ,redirect,HttpResponse
from .models import login
from .models import employeedetails
from django.contrib import messages
import MySQLdb as sql
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
check = 0

def check(request):
    global check
    try:
        if request.method == "POST":
            conn = sql.connect(host='192.168.30.93',user='root',passwd='root',db='hotel')
            cur = conn.cursor()
            data = request.POST
            #print(len(data))
            val = list(data.values())[1:]
            #print(val)
            x = 1
            for i in val:
                #print(i)
                if i == '':
                    x = 0
            #print(x)
            if x == 0:
                return render(request,"booking.html",{'data':x})
            else:
                check = val
                q="select * from rooms where no_of_bed = {} and type='{}' and status = 'NOT BOOKED'".format(int(val[2]),val[3])
                cur.execute(q)
                l = list(cur.fetchall())
                if len(l) !=0:
                    return render(request,"booking.html",{'d':l,'s':'flex'})
                else:
                    return render(request,"booking.html",{'data':1})
    except Exception as e:
        #HttpResponse(e)
        return HttpResponse('something went wrong check:'+str(e))
    return render(request,"booking.html")

def book(request):
    try:
        conn = sql.connect(host='192.168.30.93',user='root',passwd='root',db='hotel')
        cur = conn.cursor()
        data = request.POST
        x=list(data.values())[1:]
        print(x)
        if len(x) !=0:
            x = x + check[:2]
            q = "insert into book values({},'{}',{},'{}','{}','{}')".format(x[3],x[0],x[1],x[2],x[4],x[5])
            cur.execute(q)
            cur.execute("update rooms set status='BOOKED' where room_no = {}".format(x[3]))
            conn.commit()
        return render(request,"booking.html",{'s':'none'})
    except Exception as e:
        #HttpResponse(e)
        return HttpResponse('something went wrong check:'+str(e))
    return render(request,"booking.html")

def loginpage(request):
    if request.method == 'GET':
        return render(request,'loginpage.html')
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
                if dsg =='Manager':
                    return render(request,'Managerhomepage.html') 
                if dsg =='Admin':
                    return render(request,'Adminhomepage.html')
                else:
                    return render(request,'Receptionisthomepage.html')
        else:
            messages.success(request,'Invalid Details')
            return render(request,'loginpage.html')

def show(request):
    #print(request)
    try:
        conn = sql.connect(host='192.168.30.93',user='root',passwd='root',db='hotel')
        cur = conn.cursor()
        data = request.POST
        print(len(data))
        if len(data) != 0:
            d = int(list(data.keys())[1])
            #print(d)
            cur.execute('delete from book where a_room ={}'.format(d))
            cur.execute("update rooms set status='NOT BOOKED' where room_no = {}".format(d))
            conn.commit()
        cur.execute("select * from rooms where status='NOT BOOKED'")
        l = list(cur.fetchall())
        #print(l)
        cur.execute("select room_no,name,mobile_no,checkin,checkout,status from rooms inner join book on room_no = a_room order by room_no;")
        l1 = list(cur.fetchall())
        return render(request,"check.html",{'data':l,'d':l1})
    except Exception as e:
        #HttpResponse(e)
        return HttpResponse('something went wrong check:'+str(e))

def Managerhomepage(request):
    return render(request,'Managerhomepage.html')
def Adminhomepage(request):
    return render(request,'Adminhomepage.html')
def Receptionisthomepage(request):
    return render(request,'Receptionisthomepage.html')
def employeedata(request):
    return render(request,'employeedata.html')
def hotelmanager(request):
    return render(request,'hotelmanager.html')

def hotelabout(request):
    return render(request,'HOTEL_ABOUT.html')

def hotelrooms(request):
    return render(request,'HOTEL_ROOMS.html')
def hotelbooking(request):
    return render(request,'HOTEL BOOKING.html')



def employeeform(request):
    if request.method=='GET':
        return render(request,'employeeform.html')
    elif request.method=='POST':
         EMPLOYEE_ID=request.POST['EMPLOYEE_ID']
         if employeedetails.objects.filter(EMPLOYEE_ID=EMPLOYEE_ID).exists(): # it checks id is already registered or not
            messages.error(request,"Employee ID already registered !")  
            return render(request,'employeeform.html')

    else:
       employeedetails(
            EMPLOYEE_ID=request.POST.get('EMPLOYEE_ID'),
            EMPLOYEE_NAME=request.POST.get('EMPLOYEE_NAME'),
            DATE_OF_JOINING=request.POST.get('DATE_OF_JOINING'),
            SALARY=request.POST.get('SALARY'),
            MOBILE=request.POST.get('MOBILENUMBER'),
            DESIGNATION=request.POST.get('DESIGNATION'),
            GENDER=request.POST.get('GENDER')
        ).save()
       return render(request,'employeeform.html')

def adminemployeeform(request):
    if request.method=='GET':
        return render(request,'adminemployeeform.html')
    else:
       employeedetails(
            EMPLOYEE_ID=request.POST.get('EMPLOYEE_ID'),
            EMPLOYEE_NAME=request.POST.get('EMPLOYEE_NAME'),
            DATE_OF_JOINING=request.POST.get('DATE_OF_JOINING'),
            SALARY=request.POST.get('SALARY'),
            MOBILE=request.POST.get('MOBILENUMBER'),
            DESIGNATION=request.POST.get('DESIGNATION'),
            GENDER=request.POST.get('GENDER')
        ).save()
       return render(request,'adminemployeeform.html')


def empdetails(request):
    if request.method=='GET':
        empdat = employeedetails.objects.all()
        page = request.GET.get('page', 1)  #pagination
        paginator = Paginator(empdat, 5)  #displaying 5 rows in a page
        try:
            empdat = paginator.page(page)
        except PageNotAnInteger:
            empdat = paginator.page(1) #if the page is not integer it will be 1
        except EmptyPage:
            empdat = paginator.page(paginator.num_pages)
       
        return render(request, 'empdetails.html', { 'empdat': empdat })
    else:
    
    
        empdat=employeedetails.objects.all().values()
        return render(request,'empdetails.html',{'empdat':empdat})

def adminempdetails(request):
    if request.method=='GET':
        empdat = employeedetails.objects.all()
        page = request.GET.get('page', 1)  #pagination
        paginator = Paginator(empdat, 5)  #displaying 5 rows in a page
        try:
            empdat = paginator.page(page)
        except PageNotAnInteger:
            empdat = paginator.page(1) #if the page is not integer it will be 1
        except EmptyPage:
            empdat = paginator.page(paginator.num_pages)
       
        return render(request, 'adminempdetails.html', { 'empdat': empdat })
    else:
    
    
        empdat=employeedetails.objects.all().values()
        return render(request,'adminempdetails.html',{'empdat':empdat})
    









