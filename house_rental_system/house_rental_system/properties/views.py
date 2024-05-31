# properties/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Property, News
from .forms import PropertyForm
from django.shortcuts import render, redirect
from .models import Property, News
from .forms import PropertyForm
from django.http import JsonResponse
#from .mpesa import initiate_mpesa_payment
import requests
from django.conf import settings

def home(request):
    return render(request, 'properties/home.html')

def property_list(request):
    properties = Property.objects.filter(available=True)
    return render(request, 'properties/property_list.html', {'properties': properties})

def news_list(request):
    news = News.objects.all()
    return render(request, 'properties/news_list.html', {'news': news})

def post_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Property posted successfully!')
            return redirect('property_list')
        else:
            messages.error(request, 'Error posting the property. Please check the form for errors.')
    else:
        form = PropertyForm()
    return render(request, 'properties/post_property.html', {'form': form})

def property_detail(request, property_id):
    property = Property.objects.get(id=property_id)
    return render(request, 'properties/property_detail.html', {'property': property})
def landlord_portal(request):
    return render(request, 'properties/landlord_portal.html')
def tenant_portal(request):
    return render(request, 'properties/tenant_portal.html')
def contact_us(request):
    # Your view logic here
    return render(request, 'properties/contact_us.html')

def about_us(request):
    # Your view logic here
    return render(request, 'properties/about_us.html')
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property_list')  # Redirect to property list view after successful upload
    else:
        form = PropertyForm()
    return render(request, 'properties/add_property.html', {'form': form})
def mpesa_confirmation(request):
    # Handle M-Pesa confirmation callback
    # Extract data from request and update payment status
    return JsonResponse({"ResultCode": 0, "ResultDesc": "Success"})

def mpesa_validation(request):
    # Handle M-Pesa validation callback
    # Validate request data
    return JsonResponse({"ResultCode": 0, "ResultDesc": "Success"})
def initiate_payment(request):
    # Logic to get amount and phone number from the request
    amount = request.POST.get('amount')
    phone_number = request.POST.get('phone_number')
    
    response = initiate_mpesa_payment(amount, phone_number)
    def initiate_mpesa_payment(amount, phone_number):
     headers = {
        'Authorization': f'Bearer {settings.MPESA_API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
          
   "BusinessShortCode": "174379",    
   "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTYwMjE2MTY1NjI3",    
   "Timestamp":"20160216165627",    
   "TransactionType": "CustomerPayBillOnline",    
   "Amount": "1",    
   "PartyA":"254708374149",    
   "PartyB":"174379",    
   "PhoneNumber":"254708374149",    
   "CallBackURL": "https://mydomain.com/pat",    
   "AccountReference":"Test",    
   "TransactionDesc":"Test"
    }
    response = requests.post('https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', json=payload, headers=headers)
    return response.json()

def check_mpesa_payment_status(transaction_id):
    headers = {
        'Authorization': f'Bearer {settings.MPESA_API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": settings.MPESA_SECURITY_CREDENTIAL,
        "Timestamp": "20220101000000",
        "CheckoutRequestID": transaction_id
    }
    response = requests.post('https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query', json=payload, headers=headers)
    return response.json()