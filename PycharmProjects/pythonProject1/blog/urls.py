from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('post/<int:pk>/',views.PostDV.as_view(), name='post_detail'),
]