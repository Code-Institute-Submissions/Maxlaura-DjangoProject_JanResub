# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.signals import user_logged_in

# Create your models here

# News Model
class Newses(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    premium = models.BooleanField()
    date = models.DateTimeField()

# CustomUser Model
class CustomUser(models.Model):
    email = models.CharField(max_length=50)
    premium = models.BooleanField(default=False)

def save_user_in_session(sender, user, request, **kwargs):
    request.session['usermail'] = user.email

user_logged_in.connect(save_user_in_session)