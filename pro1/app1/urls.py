from django.urls import path
from .views import *

urlpatterns=[
    path("hv/",hview),
    path("studvi/",studview),
    path("sv/",showview),
    path("uv/<int:pk>/",updateview),
    path("dv/<int:x>/",deleteview)
]