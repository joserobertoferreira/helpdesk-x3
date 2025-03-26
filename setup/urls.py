from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('accounts.urls', namespace='accounts')),
    path('tickets/', include('tickets.urls', namespace='tickets')),
    path('admin/', admin.site.urls),
]
