from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^places$', views.places),
    url(r'^activity$', views.activity),
    url(r'^gallery$', views.gallery),
    url(r'^newsletter$', views.newsletter),
    url(r'^subscribe$', views.subscribe),
    url(r'^trip$', views.trip),
    url(r'^accomodation$', views.accomodation),
    url(r'^save$', views.save),
    url(r'^register$', views.register),
    url(r'^save1$', views.save1),
    url(r'^save2$', views.save2),
    url(r'^login$', views.login),
    url(r'^applogin$', views.applogin),

]
