from django.contrib import messages
from django.shortcuts import redirect, render

from accounts.forms import SignUpForm


def signup(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Usuário criado com sucesso!')
        return redirect('login')  # Redireciona para a página de login após o registro
    return render(request, 'accounts/signup.html', {'form': form})
