from django.conf.urls import url

from . import views

urlpatterns = [
	url('polls', views.index, name='index'),
	#url('/one', views.one,name="one")
]
