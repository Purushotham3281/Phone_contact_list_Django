from django.urls import path
from phone import views

urlpatterns=[
    path("insert",views.fun1),
    path("search",views.fun2),
    path("delete",views.fun3)
]