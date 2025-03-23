from django.urls import path

from contacts.views import ContactCreateView

urlpatterns = [
    path('login/', ContactCreateView.as_view(), name='login'),
]
