from django.conf.urls import url
from .views import SignUpView, HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^signup/?$', SignUpView.as_view(), name='signup')
]