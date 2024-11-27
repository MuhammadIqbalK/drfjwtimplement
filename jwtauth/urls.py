from django.urls import path

# import semua class View modul Book
from .views import (CustomLoginView, RegisterView, LogoutView, LogoutAllSessionsView)
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    # Membuat Route untuk Api endpoint Authentication
     path('login/', CustomLoginView.as_view(), name='token_obtain_pair'),
     path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('logout/', LogoutView.as_view(), name='api-logout'),
     path('logout/all', LogoutAllSessionsView.as_view(), name='api-logout-all'),
     path('register/', RegisterView.as_view(), name='api-register'),

]