from django.urls import path
from .views import RegisterView, LoginView, logout_, profile, EditView, panel, NewCourseView



app_name = 'portal'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_, name='logout'),
    path('profile/', profile, name='profile'),
    path('edit/', EditView.as_view(), name='edit'),
    path('panel/', panel, name='panel'),
    path('new-course/', NewCourseView.as_view(), name='new-course'),
]