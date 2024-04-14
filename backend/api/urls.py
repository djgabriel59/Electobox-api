from django.urls import path, include
from .views import CreateQRView, CreateUserView, DeleteQrView, GetQRView, GetUsersView, UpdateDeleteUserView, UpdateQRView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('auth/register/', CreateUserView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('users/', GetUsersView.as_view(), name='users'),
    path('users/<int:pk>/', UpdateDeleteUserView.as_view(), name='update-delete-user'),
    path('qrcodes/', CreateQRView.as_view(), name='qr-codes'),
    # path('', GetQRView.as_view(), name='get-qr-codes'),
    path('qrcodes/<int:pk>/', GetQRView.as_view(), name='update-delete-qr'),
    path('qrcodes/edit_qr/<int:pk>/', UpdateQRView.as_view(), name='delete-qr'),
    path('qrcodes/delete_qr/<int:pk>/', DeleteQrView.as_view(), name='delete-qr'),
    path('accounts/', include('django.contrib.auth.urls')),
]

