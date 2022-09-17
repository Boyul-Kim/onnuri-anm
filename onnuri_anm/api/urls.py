#store all urls local to app
from django.urls import path
from .views import main, intro

urlpatterns = [
    path('', main),
    path('intro', intro)
]