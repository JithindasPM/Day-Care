from django.shortcuts import render,redirect
from AdminSide.models import Driverdb,Vehicles,StaffDB,Plans
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from CareApp.models import RegistrationDB
from django.core.mail import send_mail

# Create your views here.
def Index(req):
    d=Driverdb.objects.count()
    dr=Driverdb.objects.filter(Verified='NOT_VERIFIED').count()
    drr=Driverdb.objects.filter(Verified='REJECTED').count()
    a=Plans.objects.count()
    s=StaffDB.objects.count()
    ss=StaffDB.objects.filter(Is_Verified='Pending').count()
    sss=StaffDB.objects.filter(Is_Verified='Rejected').count()
    C=RegistrationDB.objects.count()
    admin=User.objects.all()
    return render(req,"Index.html",{'d':d,'a':a,'s':s,'c':C,'dr':dr,'drr':drr,'sss':sss,'ss':ss,'admin':admin})

def Registration(req):
    return render(req,"Admin Registeration.html")

def Login(req):
    return render(req,"Login.html")

def Drivers_List(req):
    x=Driverdb.objects.all()
    return render(req,"Drivers List.html",{'x':x})

def Single_Driver(req,infoid):
    cab=Driverdb.objects.get(id=infoid)
    choices=Driverdb.STATUS_CHOICES
    y=Vehicles.objects.all()
    return render(req,"Driver Verification Page.html",{'cab':cab,'choices':choices,'y':y})

def Driver_Revert_Updation(req,dataid):
    if req.method=="POST":
        status=req.POST.get('status')
        msg=req.POST.get('message')
        v=req.POST.get('vehicle')
        print(v)
        Driverdb.objects.filter(id=dataid).update(Verified=status,Message=msg,Vehicle_Num=v)
        return redirect(Drivers_List)

def Delete_driver(req,dataid):
    x=Driverdb.objects.filter(id=dataid)
    x.delete()
    return redirect(Drivers_List)

##############################
def Admin_registration(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.create_superuser(username, email, password)
            subject = 'Registration Successful'
            message = f'Dear {username},\n\nYour registration with our LITTLE LEARNERS platform was successful.'
            from_email = 'aadhivish67890@gmail.com'  
            to_email = [email]
            send_mail(subject, message, from_email, to_email)
            return redirect(Login) 
        except Exception as e:
            messages.error(request,e)
            return redirect(Login)    

    return redirect(Registration)



def login_save(request):
    if request.method=="POST":
        unm=request.POST.get('username')
        pwd=request.POST.get('password')
        if User.objects.filter(username__contains=unm).exists():
            user=authenticate(username=unm,password=pwd)
            if user is not None:
                login(request,user)
                request.session['username']=unm
                request.session['password']=pwd
                messages.success(request, "Logged In Succesfully")
                return redirect(Index)
            else:
                messages.warning(request, "Please Check Your Credentials")
                return redirect(Login)
        else:
            messages.warning(request, "Please Check Your Credentials")
            return redirect(Login)
    else:
        messages.warning(request, "Please Check Your Credentials")
        return redirect(Login)
    

def Logout_Admin(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logged Out Successfully")
    return redirect('Home')
#######################################
    

def Add_vehicle(req):
    return render(req,"Add Vehicle.html")

def Save_Vehicle(req):
    if req.method=="POST":
        vn=req.POST.get('Vehicle_Num')
        mod=req.POST.get('Model')
        col=req.POST.get('Colour')
        x=Vehicles(Vehicle_Num=vn,Model=mod,Color=col)
        x.save()
        return redirect(Add_vehicle)
    
########################################

from CareApp.models import RegistrationDB

def StaffDashboard(req):
    phone_number = req.session.get('Phone')
    password = req.session.get('Password')

    try:
        staff_member = StaffDB.objects.get(Phone=phone_number, Password=password)
    except StaffDB.DoesNotExist:
        return redirect(Staff_Login_Page)
    
    data=RegistrationDB.objects.all()

    staff_name = staff_member.Staff_Name
    is_verified = staff_member.Is_Verified
    return render(req,"Staff Dashboard.html",{'staff_name':staff_name, 'Is_Verified': is_verified,'data':data})


def StaffList(req):
    x=StaffDB.objects.all()
    return render(req,"Staff List.html",{'x':x})

def Staff_Profile(req):
    phone_number = req.session.get('Phone')
    password = req.session.get('Password')

    try:
        staff_member = StaffDB.objects.get(Phone=phone_number, Password=password)
    except StaffDB.DoesNotExist:
        return redirect(Staff_Login_Page)

    staff_name = staff_member.Staff_Name
    x=StaffDB.objects.get(Phone=req.session['Phone'])
    return render(req,"Staff Profile.html",{'x':x,'staff_name':staff_name})

def Update_Staff_Password(req,dataid):
    if req.method=="POST":
        stat=req.POST.get('pwd')
        StaffDB.objects.filter(id=dataid).update(Password=stat)
        return redirect(StaffDashboard)


def Staff_Registration(req):
    return render(req,"Register Staff.html")

def Staff_Login_Page(req):
    return render(req,"Staff Login.html")

def Save_staff(req):
    if req.method=="POST":
        vn=req.POST.get('Fname')
        ph=req.POST.get('mob')
        mod=req.POST.get('loc')
        addr=req.POST.get('addr')
        pas=req.POST.get('pwd')
        x=StaffDB(Staff_Name=vn,Location=mod,Phone=ph,Address=addr,Password=pas)
        x.save()
        return redirect(Staff_Login_Page)
    


    
def StaffLogin(request):
    if request.method=="POST":
        ph=request.POST.get('Phone')
        pwd=request.POST.get('password')
        if StaffDB.objects.filter(Phone=ph,Password=pwd).exists():
            request.session['Phone']=ph
            request.session['Password']=pwd
            return redirect(StaffDashboard)
        else:
            messages.warning(request, "Check Your Credentials OR You are not a Verified User")
            return redirect(Staff_Login_Page)
    else:
        messages.warning(request, "Check Your Credentials Or Sign Up ")
        return redirect(Staff_Login_Page)
    
# def Staff_Logout(request):
#     del request.session['Phone']
#     del request.session['Password']
#     messages.success(request, "Logged Out Successfully")
#     return redirect('Home')
def Staff_Logout(request):
    request.session.flush()  # Clears all session data
    messages.success(request, "Logged Out Successfully")
    return redirect('Home')

def Single_Staff(req,dataid):
    x=StaffDB.objects.get(id=dataid)
    choices=StaffDB.STATUS
    return render(req,"Single staff detail.html",{'x':x,'choices':choices})

def Update_Staff_Status(req,dataid):
    if req.method=="POST":
        stat=req.POST.get('status')
        StaffDB.objects.filter(id=dataid).update(Is_Verified=stat)
        return redirect(Index)
    



def Delete_Staff(req,dataid):
    x=StaffDB.objects.filter(id=dataid)
    x.delete()
    return redirect(StaffList)




###############################

def addPlans(req):
    return render(req,"Add Plans.html")

def Save_plan(req):
    if req.method=="POST":
        pl=req.POST.get('planname')
        pr=req.POST.get('Price')
        ag=req.POST.get('Age')
        des=req.POST.get('des')
        x=Plans(Plan_Name=pl,Age_Group=ag,Price=pr,Plan_Description=des)
        x.save()
        return redirect(addPlans)
    
def Edit_Plan(req,infoid):
    x=Plans.objects.get(id=infoid)
    return render(req,"Edit Plan.html",{'x':x})

def Display_plans(req):
    x=Plans.objects.all()
    return render(req,"Display Plan.html",{'x':x})

def Delete_Plan(req,infoid):
    x=Plans.objects.filter(id=infoid)
    x.delete()
    return redirect(Display_plans)

def Update_plan(req,infoid):
    if req.method=="POST":
        pl=req.POST.get('planname')
        pr=req.POST.get('Price')
        ag=req.POST.get('Age')
        des=req.POST.get('des')
        Plans.objects.filter(id=infoid).update(Plan_Name=pl,Age_Group=ag,Price=pr,Plan_Description=des)
        
        return redirect(Display_plans)
    
##################################################
    
def Children_display(req):
    x=RegistrationDB.objects.all()
    return render(req,"Children List.html",{'x':x})

def single_Children(req,infoid):
    x=RegistrationDB.objects.get(Id=infoid)
    y=Driverdb.objects.filter(Verified='VERIFIED')
    return render(req,"Children Single.html",{'x':x,'y':y})

def Assign_driver(req,infoid):
    if req.method=="POST":
        dr=req.POST.get('driver')
        RegistrationDB.objects.filter(Id=infoid).update(driver=dr)
        return redirect(Children_display)


from CareApp.models import Payment
from django.views.generic import View
class Add_plans_View(View):
    def get(self,request,*args,**kwargs):
        data=Payment.objects.all().order_by('-id')
        return render(request,'user_plans.html',{'data':data})