from .models import QRCode, User
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .forms import QRCodeForm

# Create your views here.

class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class GetUsersView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class UpdateDeleteUserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class CreateQRView(LoginRequiredMixin, CreateView, ListView):
    template_name = 'index.html'
    form_class = QRCodeForm
    success_url = '/api/v1/qrcodes'
    login_url = '/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_queryset(self):
        return QRCode.objects.filter(creator=self.request.user)


class GetQRView(DetailView):
    template_name = 'qrlist.html'
    model = QRCode

class DeleteQrView(DeleteView):
    model = QRCode
    template_name = 'delete_qr.html'
    success_url = '/api/v1/qrcodes'


class UpdateQRView(UpdateView):
    model = QRCode
    form_class = QRCodeForm
    success_url = '/api/v1/qrcodes'
    template_name = 'index.html'
