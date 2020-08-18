# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Newses
from .models import CustomUser
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe

from django.shortcuts import render

# Create your views here.
def get_news_list (request):
    newses = Newses.objects.filter(premium=False)
    context = {
        'newses' : newses
    }
    return render(request, "newspaper/index.html", context)

def get_premium_news (request):

    premium = False

    if request.user.is_authenticated:
        user = request.user
        _customUser = CustomUser.objects.filter(email=user.email).first()
        if _customUser:
            premium = _customUser.premium
    newses = []
    if premium:
        newses = Newses.objects.filter(premium=True)

    context = {
        'user_premium': premium,
        'newses' : newses
    }
    return render(request, "newspaper/premium.html", context)

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def checkout_session(request):
    if request.method == 'GET':
        domain_url = 'https://newsdemoapp.herokuapp.com/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                metadata={"usermail":request.session['usermail']},
                mode='payment',
                line_items=[
                    {
                        'name': 'News paper subscription',
                        'quantity': 1,
                        'currency': 'SEK',
                        'amount': "10000",
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

def success (request):
    _customUser = CustomUser()
    _customUser.email = request.user.email
    _customUser.premium = True
    _customUser.save()
    return render(request, "success.html")

def cancel (request):
    _customUser = CustomUser()
    _customUser.email = request.user.email
    _customUser.premium = False
    _customUser.save()
    return render(request, "cancel.html")

def premium_news_success (request):
    request.from_success_payment = True
    return get_premium_news(request)