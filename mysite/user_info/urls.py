from django.conf.urls import url
import views
urlpatterns=[
    url(r'^index/$',views.index,name='index'),
    url(r'^login/$',views.login),
    url(r'^register/$',views.register),
    url(r'^register_hand/$',views.registerHand),
    url(r'^uname_verify/$',views.uname_verify),
    url(r'^loginHand/$',views.loginHand),
]
