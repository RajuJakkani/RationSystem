from django.shortcuts import render
from django.http import HttpResponse
from .models import ShopKeeper, Clients, History
from django.shortcuts import redirect
import random
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from twilio.rest import Client
from .models import Feedback as fd
from .forms import MyForm

# SMS
 #raju
TWILIO_NUMBER = "+15077097637"
#mukund
# TWILIO_NUMBER = "+15075688087" 
# TWILIO_NUMBER = "+15074178219"
# TO_NUMBER = "+918263994073"

# account_sid = "ACc936171780b838db093fa75848a20daa"
# auth_token = "c4895920e134247d2b1fe40f40ba33aa"

#raju
account_sid = "ACaf64350082bb2570fcfda26637a7efaa"
auth_token = "4f55554e9ffe593a8d97da5fc54fa2a8"

# account_sid = "AC5e8d5116cffac2b2c9e452abd99691c0"
# auth_token = "24bbe1b20ae3fbd8b3cd80ce1dc9ce5d"

t_client = Client(account_sid, auth_token)

# global stuff
shopkeeper_data = None
client = None
OTP = None

#utils
def generateOTP():
    temp = ""
    for _ in range(4):
        temp += str(random.randint(0, 9))
    return temp

# Create your views here.

@csrf_exempt
def index(request):
    data = ShopKeeper.objects.all()
    shopkeeper_data = {
        "username": data[0].username,  
        "password": data[0].password, 
        "shop_number": data[0].shop_number, 
        "mobile_number": data[0].mobile_number,
        "rice_purched": data[0].rice_purched,
        "dal_purched": data[0].dal_purched,
        "dal_alloted": data[0].dal_alloted,
        "sugar_purched": data[0].sugar_purched,
        "sugar_alloted": data[0].sugar_alloted,
        "wheat_purched": data[0].wheat_purched,
        "wheat_alloted": data[0].wheat_alloted,
    }
        
    if request.POST:
        print(request.POST)
        username = request.POST['UserName']
        password = request.POST['password']
        if username == shopkeeper_data['username'] and password == shopkeeper_data['password']:
            return redirect('/shopkeeper')
            
        
    return render(request ,"home/Login.html")


def grain(request):
    data = {
        "rice": random.randint(1, 20),
        "rice_price": random.randint(10, 30),
        "dal": random.randint(1, 20),
        "dal_price": random.randint(10, 30),
        "sugar": random.randint(1, 20),
        "sugar_price": random.randint(10, 30),
        "wheat": random.randint(1, 20),
        "wheat_price": random.randint(10, 30),
    }
    return render(request ,"home/allotedGrains.html", {"data": data})

def members(request):
    return render(request ,"home/MemberDetails.html")

def shopkeeper(request):
    data = ShopKeeper.objects.all()
    shopkeeper_data = {
        "username": data[0].username, 
        "password": data[0].password, 
        "shop_number": data[0].shop_number, 
        "mobile_number": data[0].mobile_number,
        "rice_purched": data[0].rice_purched,
        "dal_purched": data[0].dal_purched,
        "dal_alloted": data[0].dal_alloted,
        "sugar_purched": data[0].sugar_purched,
        "sugar_alloted": data[0].sugar_alloted,
        "wheat_purched": data[0].wheat_purched,
        "wheat_alloted": data[0].wheat_alloted,
    }
    global client
    if request.POST:
        client_data = Clients.objects.all()
        client_data = client_data.filter(RCN=request.POST['RCN'])
        client = {
            "name":client_data[0].name,
            "gender": client_data[0].gender,
            "age": client_data[0].age,
            "status": client_data[0].status,
            "district": client_data[0].district,
            "UID": client_data[0].UID,
            "RCN": client_data[0].RCN
        }
        
    return render(request, "home/shopkeeper.html", {"client": client, "shopkeeper": shopkeeper_data})


def client(request):
    global client
    if request.POST:
        client_data = Clients.objects.all()
        client_data = client_data.filter(RCN=request.POST['RCN'])
        client_id = Clients.objects.get(RCN=request.POST['RCN'])
        client_history = History.objects.filter(client=client_id)
        print(client_history)
        client = {
            "name":client_data[0].name,
            "gender": client_data[0].gender,
            "age": client_data[0].age,
            "status": client_data[0].status,
            "district": client_data[0].district,
            "UID": client_data[0].UID,
            "RCN": client_data[0].RCN,
            "client_history": []
        }
        for data in client_history:
            client['client_history'].append({"rice": data.rice, "dal": data.dal, "sugar": data.sugar, "wheat": data.wheat, "date": data.date})
        print(client)
        
    return render(request, "home/client.html", {"client": client})

def Feedback(request):
    if request.method == "POST":
        feedback = fd()
        client = request.POST['client']
        mobie_no=request.POST['mobie_no']
        email=request.POST['email']
        comment=request.POST['comment']
        image=request.POST['image']

        feedback.client = client
        feedback.mobie_no = mobie_no
        feedback.email = email
        feedback.comment = comment
        feedback.image = image
        feedback.save()
        print(request.POST)
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse("<h1>THANK YOU FOR YOUR FEEDBACK</h1>")

    else:
        form = MyForm()
    return render(request ,"home/feedback.html",{"form":form})

def history(request):
    return render(request ,"home/history.html")

@csrf_exempt
def verification(request):
    global OTP

    if (request.method == "POST"):
        if (request.POST.get('flag') == "1"):
            print(request.POST.get('user_id'))
            print(request.POST.get('opt'))
            print(request.POST.get('flag'))
            print(request.POST.get('dal'))
            print(request.POST.get('rice'))
            print(request.POST.get('sugar'))
            print(request.POST.get('wheat'))
            print("OPT", OTP)
            print("opt", request.POST.get('opt'))

            if (str(request.POST.get('opt')) == OTP):
                rice = request.POST.get('rice')
                dal = request.POST.get('dal')
                sugar = request.POST.get('sugar')
                wheat = request.POST.get('wheat')
                client_id = Clients.objects.get(RCN=request.POST.get('user_id'))
                history = History(rice=rice, sugar=sugar, wheat=wheat, dal=dal, client=client_id)
                history.save()

                return JsonResponse({"flag": "1"})
            else:
                return JsonResponse({"flag": "0"})
            
        elif (request.POST.get('flag') == "0"):
            user_id = request.POST.get('user_id')
            rice = request.POST.get('rice')
            dal = request.POST.get('dal')
            sugar = request.POST.get('sugar')
            wheat = request.POST.get('wheat')
            client = Clients.objects.get(RCN=user_id)
            print(client.phone)
            PHONE_NUMBER = "+91"
            PHONE_NUMBER += client.phone
            print(PHONE_NUMBER)
            OTP = generateOTP()
            print(OTP)

            # Code to send OPT    
            message = t_client.messages.create(
                body=f'Your OTP for E Ration is {OTP} Rice : {rice} , Dal : {dal}, Wheat : {wheat}, Sugar : {sugar}',
                from_ = TWILIO_NUMBER,
                to = PHONE_NUMBER
            )

    return render(request, "home/verification.html")