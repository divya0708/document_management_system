from django.conf.urls import include,url
from documents import views
urlpatterns = [
	url(r'^form/$', views.Form),
	url(r'^upload/$', views.Upload),
	]