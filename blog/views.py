from django.core.urlresolvers import reverse
from django.views.generic import FormView, TemplateView
from .forms import SignUpForm


class SignUpView(FormView):
    form_class = SignUpForm
    success_url = '/blog'
    template_name = 'blog/signup.html'


class HomeView(TemplateView):
    template_name = 'blog/home.html'


class LoginView(FormView):
    pass
