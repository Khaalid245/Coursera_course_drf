from django.urls import path
from .import views

urlpatterns = [
  
    path('Book/', views.BookView.as_view()),
    path('books/<int:pk>', views.SingleBookView.as_view(), name='SingleBook'),

    
]