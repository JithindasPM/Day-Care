from django.shortcuts import render,redirect
from CareApp.models import RegistrationDB,Rating,Payment
import DriverApp.views
from AdminSide.models import Plans
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail

# Create your views here.

def Children_Form(request):
    
    return render(request,"Children_Registration.html")

def Registration_save(request):
    if request.method=="POST":
        fi_nm=request.POST.get('first_name')
        las_nm=request.POST.get('last_name')
        uname=request.POST.get('uname')
        par_nm=request.POST.get('Parents_Name')
        pas=request.POST.get('pwd')
        mail=request.POST.get('your_email')
        ph=request.POST.get('phone')
        addr=request.POST.get('street')
        loc=request.POST.get('additional') 
        pickup=request.POST.get('pickup')
        drop=request.POST.get('drop')
        medi_his=request.POST.get('medical')
        aller=request.POST.get('aller')
        spl_att=request.POST.get('Spl_att')
        emger=request.POST.get('emer')
        im=request.FILES['img']
        x=RegistrationDB(First_Name=fi_nm,
                       Last_Name=las_nm,
                       Password=pas,
                       Username=uname,
                       Mail=mail,
                       Parents_Name=par_nm,
                       Phone=ph,
                       Address=addr,
                       Location=loc,
                       Pickup_Point=pickup,
                       Drop_Point=drop,
                       Medical_History=medi_his,
                       Alleries=aller,
                       Special_Attention=spl_att,
                       Emergency_Procedures=emger,
                       Kid_Image=im)
        x.save()
        subject = 'Registration Successful'
        message = f'Dear {fi_nm},\n\nYour registration with our LITTLE LEARNERS platform was successful.'
        from_email = 'aadhivish67890@gmail.com'  
        to_email = [mail]
        send_mail(subject, message, from_email, to_email)
        return redirect(ParentsLogin)
    
def ParentsLogin(req):
    return render(req,"Parents Login.html") 

def Home(req):
    y=Rating.objects.all().order_by('-id')[:4]
    if 'Username' in req.session:
        x=RegistrationDB.objects.get(Username=req.session['Username'])
        return render(req,"Dashboard.html",{'x':x,'y':y})
    else:
        return render(req,"Dashboard.html",{'y':y})

def About(req):
    return render(req,"About.html")

def Profile(req):
    x=RegistrationDB.objects.get(Username=req.session['Username'])
    return render(req,"Profile.html",{'x':x})


def Parents_Login_save(request):
    if request.method=="POST":
        Em=request.POST.get('uname')
        pwd=request.POST.get('password')
        if RegistrationDB.objects.filter(Username=Em,Password=pwd).exists():
            request.session['Username']=Em
            request.session['Password']=pwd
            print('======================')
            return redirect(Home)
        else:
            messages.warning(request," ")
            print('-------------------------')
            return redirect(ParentsLogin)
    else:
        messages.warning(request, " ")
        return redirect(ParentsLogin)
    
def Update_Registration(request,infoid):
    if request.method=="POST":
        fi_nm=request.POST.get('First_Name')
        las_nm=request.POST.get('Last_Name')
        par_nm=request.POST.get('Parents_Name')
        ph=request.POST.get('Phone')
        addr=request.POST.get('Address')
        loc=request.POST.get('Location') 
        pickup=request.POST.get('Pickup_Point')
        drop=request.POST.get('Drop_Point')
        medi_his=request.POST.get('Medical_History')
        aller=request.POST.get('Allergies')
        spl_att=request.POST.get('Special_Attention')
        emger=request.POST.get('Emergency_Procedures')
        try:
            im=request.FILES['Kid_Image']
            a=FileSystemStorage()
            b=a.save(im.name,im)
        except MultiValueDictKeyError:
            b=RegistrationDB.objects.get(Id=infoid).Kid_Image
        RegistrationDB.objects.filter(Id=infoid).update(First_Name=fi_nm,
                       Last_Name=las_nm,
                       Parents_Name=par_nm,
                       Phone=ph,
                       Address=addr,
                       Location=loc,
                       Pickup_Point=pickup,
                       Drop_Point=drop,
                       Medical_History=medi_his,
                       Alleries=aller,
                       Special_Attention=spl_att,
                       Emergency_Procedures=emger,Kid_Image=b)
        return redirect(Home)

        
# def Parents_Logout(request): 
#     if 'Username' in request.session:
#         del request.session['Username']
#     messages.success(request, "Logged Out Successfully")
#     return redirect(Home)

def Parents_Logout(request): 
    request.session.flush()  # Clears all session data
    messages.success(request, "Logged Out Successfully")
    return redirect(Home)


def Update_Route(req,dataid):
    if req.method=="POST":
        pic=req.POST.get('pickup')
        drop=req.POST.get('dropoff')
        dat=req.POST.get('date')
        ti=req.POST.get('PickUpTime')
        RegistrationDB.objects.filter(Id=dataid).update(time_field=ti,date_field=dat,Temp_Pickup_Point=pic,Temp_Drop_Point=drop)
        return redirect(Home)


def View_Plans(req):
    x=Plans.objects.all()
    return render(req,"View Plans Frontend.html",{'x':x})

def rating_save(req):
    if req.method=="POST":
        un=req.POST.get('uname')
        pa=req.POST.get('parents')
        des=req.POST.get('des')
        x=Rating(Username=un,Parents_Name=pa,Description=des)
        x.save()
        return redirect(Home)

def Payment_pg(req,dataid):
    x=Plans.objects.get(id=dataid)
    return render(req,"Payment.html",{'x':x})

def Payment_save(req):
    if req.method=="POST":
        card_nm=req.POST.get('crdnum')
        card_nam=req.POST.get('crdname')
        Amt=req.POST.get('amt')
        Exp=req.POST.get('exp')
        cvv=req.POST.get('cv')
        customer_uname = req.POST.get('customer')
        num= req.POST.get('id')
        num_id = Plans.objects.filter(id=num).first()
        customer = RegistrationDB.objects.filter(Username=customer_uname).first()
        if customer is None:
            messages.warning(req,"No Customer With Registered Mail")
        x=Payment(CardHolder_Name=card_nam,Card_Num=card_nm,Amount=Amt,Booking_Date=Exp,CVV=cvv,Customer_ID=customer,Plan_ID=num_id)
        x.save()
        messages.success(req,"Amount Paid Successfully")
        return redirect('Home')
    
# def Purchase_List(req):
#     x=Payment.objects.filter(Username=req.session['Username'])
#     return render(req,"Purchase List.html",{'x':x})


import groq
import re

client = groq.Client(api_key="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")


def get_groq_response(user_input):
    """
    Communicate with the GROQ chatbot to get a response based on user input.
    """
    system_prompt = {
        "role": "system",
        "content": "You are a helpful assistant.Keep your answers short and to the point ."
    }

    chat_history = [system_prompt]

    # Append user input to the chat history
    chat_history.append({"role": "user", "content": user_input})

    # Get response from GROQ API
    chat_completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=chat_history,
        max_tokens=100,
        temperature=1.2
    )

    response = chat_completion.choices[0].message.content
    print(response)
    # Format response (convert *bold* to <b>bold</b>)
    response = re.sub(r'\\(.?)\\*', r'<b>\1</b>', response)

    return response

from django.views.generic import View
from CareApp.forms import Groq_Chat_Form
    
class Groq_View(View):
    def get(self, request, *args, **kwargs):
        form = Groq_Chat_Form()
        # Start with fresh chat history
        request.session['chat_history'] = []
        return render(request, 'chat.html', {'form': form, 'chat_history': []})
    
    def post(self, request, *args, **kwargs):
        form = Groq_Chat_Form(request.POST)
        user_input = request.POST.get('text')

        if not user_input:
            message = 'Please enter a message'
            return render(request, 'chat.html', {
                'error': message, 
                'form': form, 
                'chat_history': request.session.get('chat_history', [])
            })

        # Get response from Groq
        chatbot_response = get_groq_response(user_input)
        
        # Get existing chat history or initialize empty list
        chat_history = request.session.get('chat_history', [])
        
        # Add new messages to history
        chat_history.append({
            'user': user_input,
            'bot': chatbot_response
        })
        
        # Update session
        request.session['chat_history'] = chat_history
        request.session.modified = True
        
        form = Groq_Chat_Form()
        return render(request, 'chat.html', {
            'form': form, 
            'chat_history': chat_history
        })
       
       
from .models import Chat
from .forms import ChatMessageForm
from AdminSide.models import StaffDB

def chat_view(request):
    messages = Chat.objects.order_by("timestamp") 
    current_user = None
    
    if request.session.get('Username'):
        current_user = request.session.get('Username')
    elif request.session.get('Phone'):
        b = request.session.get('Phone') 
        data = StaffDB.objects.get(Phone=b)
        current_user = data.Staff_Name

    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.user = current_user
            chat_message.save()
            return redirect("chat") 
    else:
        form = ChatMessageForm()

    return render(request, "chat_form.html", {
        "messages": messages, 
        "form": form,
        "current_user": current_user
    })
    
    
import random
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import RegistrationDB
from django.http import JsonResponse

otp_storage = {}  # Temporary storage for OTPs

def forgot_password(request):
    if request.method == "POST":
        username = request.POST.get("username")
        try:
            user = RegistrationDB.objects.get(Username=username)
            otp = random.randint(100000, 999999)  # Generate a 6-digit OTP
            otp_storage[username] = otp  # Store OTP temporarily

            # Send OTP to the user's registered email
            send_mail(
                "Password Reset OTP",
                f"Your OTP for password reset is {otp}",
                "your_email@example.com",  # Replace with your email
                [user.Mail],
                fail_silently=False,
            )
            request.session["reset_username"] = username  # Store username in session
            return JsonResponse({"status": "success", "message": "OTP sent to your email."})

        except RegistrationDB.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Username not found!"})

    return render(request, "forgot_password.html")

def verify_otp(request):
    if request.method == "POST":
        username = request.session.get("reset_username")
        entered_otp = int(request.POST.get("otp"))

        if username in otp_storage and otp_storage[username] == entered_otp:
            return JsonResponse({"status": "success", "message": "OTP verified!"})
        else:
            return JsonResponse({"status": "error", "message": "Invalid OTP!"})

    return render(request, "verify_otp.html")

def reset_password(request):
    if request.method == "POST":
        username = request.session.get("reset_username")
        new_password = request.POST.get("new_password")

        try:
            user = RegistrationDB.objects.get(Username=username)
            user.Password = new_password  # Store password in plain text (not secure)
            user.save()
            del otp_storage[username]  # Remove OTP from storage
            return JsonResponse({"status": "success", "message": "Password updated successfully!"})

        except RegistrationDB.DoesNotExist:
            return JsonResponse({"status": "error", "message": "User not found!"})

    return render(request, "reset_password.html")
