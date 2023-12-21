from django.urls import path
from .views import Create_person, show_persons, retrieve_person, delete_person, update_person

urlpatterns = [
    path('create/', Create_person),
    path('show/', show_persons),
    path('retrieve/<int:pk>/', retrieve_person),
    path('update/<int:pk>/', update_person),
    path('delete/<int:pk>/', delete_person)
]