from django.urls import reverse_lazy
from django.views import generic

from users.forms import SignUpForm


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('users:login')
