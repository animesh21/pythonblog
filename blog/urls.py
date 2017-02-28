from django.conf.urls import url
from .views import sign_up_view, HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^signup/?$', sign_up_view, name='signup')
]