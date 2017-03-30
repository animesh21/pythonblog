from django.conf.urls import url
from .views import sign_up_view, login_view, home

app_name = 'blog'
urlpatterns = [
    url(r'^signup/?$', sign_up_view, name='signup'),
    url(r'^login/?$', login_view, name='login'),
    url(r'^home/?$', home, name='home'),
]