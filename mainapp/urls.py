from django.urls import path
from .views import register_emps, get_emps, alter_emps
urlpatterns=[
    path('register-emps/', register_emps.handle),
    path('get-emps', get_emps.handle),
    path('alter-emps/', alter_emps.handle),
]