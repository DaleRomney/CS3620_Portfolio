from . import views
from django.urls import path

app_name = 'PortfolioDatabase'
urlpatterns = [
    path('', views.index, name="index"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('contact/', views.contact, name="contact"),
    path('<int:item_id>', views.h_details, name="h_details"),
    path('<int:item_id>', views.p_details, name="p_details"),
]