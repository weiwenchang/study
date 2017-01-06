from django.conf.urls import include, url

import views

urlpatterns = [
    url(r'^ucinfo/$', views.ucInfo, name='ucInfo'),
    url(r'^ucaddress/$', views.ucAddress, name='ucAddress'),
    url(r'^getAddressInfo/$',views.getAddressInfo)
]