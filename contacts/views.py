from django.shortcuts import redirect, render

from contacts.forms import ContactForm
from contacts.models import Contact


def index(request):
    contacts = Contact.objects.all()
    context = {'contacts': contacts}
    return render(request, 'contacts/index.html', context)


def register(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        code = form.cleaned_data.get('code')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')

    return redirect('login')
