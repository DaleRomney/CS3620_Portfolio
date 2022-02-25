from . import views
from django.urls import path

app_name = 'PortfolioDatabase'
urlpatterns = [
    path('', views.index, name="index"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('contact/', views.contact, name="contact"),
    path('hobbies/<int:item_id>', views.h_details, name="h_details"),
    path('portfolio/<int:item_id>', views.p_details, name="p_details"),
    path('add/', views.add_item, name="add_item"),
    path('update/<int:id>', views.update_item, name="update_item"),
    path('delete/<int:id>', views.delete_item, name="delete_item"),
    path('create_contact', views.create_contact, name="create_contact"),
]