# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Newses
from .models import CustomUser

# Register your models here.
admin.site.register(Newses)
admin.site.register(CustomUser)