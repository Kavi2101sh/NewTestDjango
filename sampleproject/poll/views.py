# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from poll.models import AccessRecord, Topic, Webpage

def index(request):
	new_dict={
	"insert_me": "from index function to index.html"
	}
	return render(request, "poll/index.html", context=new_dict)

def one(request):
	return HttpResponse("this one is working as well")

def two(request):
	webpages_list = AccessRecord.objects.order_by('date')
	date_dict = {'access_records': webpages_list}
	return render(request,"poll/index.html",context =  date_dict)