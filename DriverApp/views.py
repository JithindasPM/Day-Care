from django.shortcuts import render,redirect
from AdminSide.models import Driverdb
from django.http import HttpResponse
from django.contrib import messages
from AdminSide.views import Index
from django.core.mail import send_mail
from CareApp.models import RegistrationDB


# Create your views here.

def Driver_Form(req):
    return render(req,"Driver_Registration.html")

def Driver_Login(req):
    return render(req,"Driver_Login.html")


def Driver_Registration_save(req):
    if req.method=="POST":
        fn=req.POST.get('Fname')
        mob=req.POST.get('mob')
        un=req.POST.get('uname')
        en=req.POST.get('email')
        add1=req.POST.get('addr1')
        add2=req.POST.get('addr2')
        pin=req.POST.get('zip')
        pas=req.POST.get('pwd')
        idno=req.POST.get('Proof_Id')
        img=req.FILES['IDImage']
        if Driverdb.objects.filter(Username=un).exists():
            return HttpResponse("Username Already Exists")
        elif Driverdb.objects.filter(Email=en).exists():
            return HttpResponse("Email Already Exists")
        elif Driverdb.objects.filter(License_Number=idno).exists():
            return HttpResponse("Enter Valid ID Number")
        else:
            x = Driverdb(Name=fn, Password=pas, Mobile=mob, Username=un, Email=en,
                         Address1=add1, Address2=add2, Pin_Code=pin, License_Number=idno,
                         ID_Image=img)
            x.save()
            subject = 'Registration Successful'
            message = f'Dear {un},\n\nYour registration with our LITTLE LEARNERS platform was successful.'
            from_email = 'aadhivish67890@gmail.com'  
            to_email = [en]
            send_mail(subject, message, from_email, to_email)
            return redirect(Driver_Form)
        

# def Driver_Dashboard(req):
#     return render(req, "Driver Dashboard.html")


def Driver_Login_Save(request):
    if request.method=="POST":
        Em=request.POST.get('Email')
        pwd=request.POST.get('password')
        if Driverdb.objects.filter(Email=Em,Password=pwd,Verified='VERIFIED').exists():
            request.session['Email']=Em
            request.session['Password']=pwd
            return redirect(Assigned_Childrens)
        else:
            messages.warning(request, "Check Your Credentials OR You are not a Verified User")
            return redirect(Driver_Login)
    else:
        messages.warning(request, "Check Your Credentials Or Sign Up ")
        return redirect(Driver_Login)

def Driver_Profile(req):
    cab=Driverdb.objects.get(Email=req.session['Email'])
    return render(req,"Driver Profile.html",{'cab':cab})

def Driver_Logout(request):
    del request.session['Email']
    del request.session['Password']
    messages.success(request, "Logged Out Successfully")
    return redirect('Home')


def Assigned_Childrens(request):
    driver = Driverdb.objects.get(Email=request.session['Email'])
    print(driver.Name)
    x= RegistrationDB.objects.filter(driver_id=driver)
    print(x)
    return render(request,'Assigned Children.html',{'x':x,'driver':driver})

