from django.urls import path

from accounts.views import SigninView, SignoutView, SignupView

app_name = 'accounts'
urlpatterns = [
    path('', SigninView.as_view(), name='login'),
    path('register/', SignupView.as_view(), name='register'),
    path('logout/', SignoutView.as_view(), name='logout'),
]
