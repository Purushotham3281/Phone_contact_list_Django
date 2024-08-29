from django.shortcuts import render
from phone.models import Contacts

# Create your views here.
def fun1(request):
    result=Contacts.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        phone=request.POST.get("number")
        


        obj=Contacts(Name=name,Number=phone)
        obj.save()
        result=Contacts.objects.all()
        return render(request,"Insert.html",{"res":result , "obj":obj})
    return render(request,"Insert.html")



def fun2(request):
    result=Contacts.objects.all()
    if request.method=="POST":
        peru=str(request.POST.get("name"))
        if Contacts.objects.filter(Name=peru).exists():
            abc=Contacts.objects.get(Name=peru) 
        else:
            abc=None
        return render(request,"record.html",{"res":result,"res2":abc})
    return render(request,"record.html")


def fun3(request):
    
    if request.method=="POST":

        peru=request.POST.get("name")
        if Contacts.objects.filter(Name=peru):
            result=Contacts.objects.all()
            abc=Contacts.objects.get(Name=peru) 
            abc.delete()
        

   
            return render(request,"delete.html",{"result":result,"abc":abc})
    result=Contacts.objects.all()
    return render(request,"delete.html", {"result":result})





