from django.urls import path

from .views import BlogHomeView, BlogCreateView, BlogDetailView

app_name = 'blogs'

urlpatterns = [
	path('', BlogHomeView.as_view(), name='home'),
	path('new/', BlogCreateView.as_view(), name='new'),
	path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),
]
