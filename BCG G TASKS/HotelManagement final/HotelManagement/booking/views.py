from django.shortcuts import render,HttpResponse
import MySQLdb as sql

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
    
