from django.urls import path
from .views import RegisterView, LoginView, logout_, profile, EditView, search




app_name = 'appointment'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_, name='logout'),
    path('profile/', profile, name='profile'),
    path('edit/', EditView.as_view(), name='edit'),
    path('search/', search, name='search'),
]
