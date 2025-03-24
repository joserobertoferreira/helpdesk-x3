from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView

from accounts.forms import SignUpForm


class SigninView(LoginView):
    template_name = 'accounts/login.html'


class SignoutView(LogoutView):
    next_page = '/'


class SignupView(FormView):
    template_name = 'accounts/register.html'
    form_class = SignUpForm
    success_url = ''

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
