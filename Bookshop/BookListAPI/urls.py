from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books),  # ✅ this line connects the URL path to the view function
]
