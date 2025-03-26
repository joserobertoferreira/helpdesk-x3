from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views.generic import CreateView, View

from accounts.forms import SignUpForm


class SigninView(View):
    template_name = 'accounts/login.html'

    def get(self, request):
        data = {'form': AuthenticationForm, 'error': None}
        return render(request, self.template_name, data)

    def post(self, request):
        data = AuthenticationForm(request.POST or None)

        if data is not None:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('tickets:ticket_list')
        return render(
            request,
            self.template_name,
            {
                'form': data,
                'error': 'A autenticação falhou. Verifique o login, a senha e tente novamente.',
            },
        )


class SignoutView(View):
    @staticmethod
    def get(request):
        logout(request)
        return redirect('accounts:login')


class SignupView(CreateView):
    template_name = 'accounts/register.html'

    def get(self, request):
        data = {'form': SignUpForm}
        return render(request, self.template_name, data)
