# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from poll.models import AccessRecord, Topic, Webpage
from django.contrib import admin
from django.http import HttpResponse
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)

