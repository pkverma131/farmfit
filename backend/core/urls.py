from django.urls import path
from . import views

urlpatterns = [
    path('crops/', views.crop_list),
    # path('crop/<int:pk>/', views.crop_detail),
]