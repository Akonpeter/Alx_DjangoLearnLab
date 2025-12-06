from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .form import RegisterForm

class CustomLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        return super().form_valid(form)
