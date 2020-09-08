from django.urls import path
from . import views

urlpatterns = [path('api/refuge/', views.RefugeListCreate.as_view())]
