from . import views
from django.urls import path

urlpatterns = [
        path('', views.tweet_list, name='tweet_list'),  # Map the 'home/' URL to the homi view
        path('create/', views.tweet_create, name='tweet_create'),  # Map the 'home/' URL to the homi view
        path('<int:tweet_id>/edit/', views.tweet_delete, name='tweet_delete'),  # Map the 'home/' URL to the homi view
        path('<int:tweet_id>/delete/', views.tweet_edit, name='tweet_edit'),  # Map the 'home/' URL to the homi view
        path('register/',views.register, name='register'),  # Map the 'home/' URL to the homi view
        path('tweets/search/', views.tweet_search, name='tweet_search'),  # Add this line
        path('about-us/', views.about_us, name='about_us'),
        path('contact-us/', views.contact_us, name='contact_us'),

        ]




