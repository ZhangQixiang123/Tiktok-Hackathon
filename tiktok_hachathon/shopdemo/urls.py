from django.urls import include, path
from . import views

urlpatterns = [

]

# Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
