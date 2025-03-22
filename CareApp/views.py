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
    y=Rating.objects.all()[:4]
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
            return redirect(Home)
        else:
            messages.warning(request, "Check Your Credentials OR You are not a Verified User")
            return redirect(ParentsLogin)
    else:
        messages.warning(request, "Check Your Credentials Or Sign Up ")
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

        
def Parents_Logout(request): 
    if 'Username' in request.session:
        del request.session['Username']
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
        x=Payment(CardHolder_Name=card_nam,Card_Num=card_nm,Amount=Amt,Expiry_Date=Exp,CVV=cvv,Customer_ID=customer,Plan_ID=num_id)
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
        