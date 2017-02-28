from django.core.urlresolvers import reverse
from django.views.generic import FormView, TemplateView
from .forms import SignUpForm
from django.shortcuts import render


q
def sigh_up_view(request):


    form = SignUpForm(request.POST or None)
    context = {
        "title":"Sign up form",
        "form":form
    }

    if request.method == "POST":
        form = SignUpForm(request.POST or None)


    return render(request,"blog/signup.html", context=context)

class HomeView(TemplateView):
    template_name = 'blog/home.html'


class LoginView(FormView):
    pass
