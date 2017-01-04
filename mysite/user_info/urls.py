from django.conf.urls import url
import views
urlpatterns=[
    url(r'^login/$',views.login),
    url(r'^register/$',views.register),
    url(r'^register/register_hand/$',views.registerHand),
]
