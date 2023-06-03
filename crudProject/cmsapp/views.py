

from .models import Customerr
from django.shortcuts import render
from django.http import HttpResponse
#from .models import Customer
# Create your views here.

def hello(request):
    #resp=HttpResponse("<h1>hey world hows going</h1>")
    if request.method=='GET':
            resp=render(request,"cmsapp/home.html")
            return resp
    elif request.method=="POST":
            if 'btn_insert' in request.POST:
                    cs=Customerr()
                    cs.name=request.POST.get('txtname',"N/A")
                    cs.email=request.POST.get("txtemail","N/A")
                    cs.age=request.POST.get("txtage","NA")
                    cs.address=request.POST.get("txtaddress","NA")
                    cs.number=int(request.POST.get("txtnumber","NA"))
                    cs.save()
                    resp=HttpResponse("<h1>Data have been submitted </h1>")
                    return resp
            elif "btn_search" in request.POST:
                    cid=int(request.POST.get("txtid",0))
                    cus=Customerr.objects.get(id=cid).exits()
                    d1={'cus':cus} 
                    resp=render(request,'cmsapp/home.html',context=d1)
                    return resp
            elif "btn_show" in request.POST:
                     cxs=Customerr.objects.all()
                     d1={'cxs':cxs}
                     resp=render(request,'cmsapp/home.html',context=d1)
                     return resp
            elif "btndelete" in request.POST:
                    cus=Customerr()
                    cus.id=int(request.POST.get("txtid",0))
                    Customerr.objects.filter(id=cus.id).delete()
                    rep=HttpResponse("<h1>data is deleted</h1>")
                    return rep
            elif "btn_update" in request.POST:
                   cs=Customerr()
                   cs.id=int(request.POST.get("txtid",0))
                   if Customerr.objects.filter(id=cs.id).exists():
                           cs.name=request.POST.get("txtname",0)
                           cs.email=request.POST.get("txtemail",0)
                           cs.age=int(request.POST.get("txtage",0))
                           cs.address=request.POST.get("txtaddress",0)
                           cs.number=int(request.POST.get("txtnumber",0))
                           cs.save()
                           res=HttpResponse("<h1>update done on id ="+str(cs.id)+"</h1>")
                           return res
           ## elif "btn_profile" in request.POST:
             #       cus=Customerr.objects.all()
              #      d1={'cus':cus}
               #     resp=render(request,"cmsapp/home.html",context=d1)
                #    return resp
           ### elif "btn_select" in request.POST:
              ###      com=Customerr.objects.all()
                 ###   d4={"com":com}
                    ##reso=render(request,"cmsapp/home.html",context=d4)
                    ##return reso
                 

                   

    #elif request.method=="POST":
        #if 'btn_add' in request.POST:
                #cus=Customer()
                #cus.name=request.POST.get('txtname','NA')
                #cus.age=request.POST.get('txtage','NA')
                #cus.address=request.POST.get('txtaddress',"NA")
                #cus.mobile=request.POST.get("txtnumber","NA")
                #cus.save()
                #esp=HttpResponse("<h1>added succesfully </h1>")
                #return esp
                