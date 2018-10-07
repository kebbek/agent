from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import UserRegisterForm, LoginForm
from .models import User


def home_view(request):
    return HttpResponse('site.')


def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse_lazy('home'))


class UserRegisterView(generic.CreateView):
    model = User
    form_class = UserRegisterForm


class LoginView(generic.FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('order:list')

    def form_valid(self, form):
        phone = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(phone=phone, password=password)

        if user.is_active and user is not None:
            login(self.request, user=user)
            return super().form_valid(form)
        else:
            return super().form_invalid(form)
