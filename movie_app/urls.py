from django.urls import path
from . import views
urlpatterns = [
    path('',views.list),
    path('manage',views.manage),
    path('', list, name='list'),
    path('login',views.custom_login),
    path('logout',views.logout_view),
    path('list',views.list),
    path('manage',views.manage),
    path('addmember', views.addmember, name='addmember'),
]