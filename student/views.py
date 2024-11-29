from django.shortcuts import render
import razorpay
from django.conf import settings
# Create your views here.


def home(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")



def donate(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        amount = float(request.POST.get("amount")) * 100  # Convert to paise

        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET_KEY))
        payment = client.order.create({
            'amount': amount,
            'currency': 'INR',
            'payment_capture': '1'
        })


        context = {
            "payment": payment,
            "name": name,
            "email": email,
            "amount": amount / 100,
            "key_id": settings.RAZORPAY_KEY_ID
        }
        return render(request, "pay.html", context)

    return render(request, "bill.html")