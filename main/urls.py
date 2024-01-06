from django.urls import path
from . import views

handler404 = 'main.views.custom_404'  # Replace 'main.views.custom_404' with your view function path

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.quote_detail, name='quote_detail'),
    path('past-quotes/', views.past_quotes, name='past_quotes'),
]
