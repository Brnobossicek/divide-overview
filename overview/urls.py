from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    #path("<str:s>/", TemplateView.as_view(template_name="index.html")),
    #path('accounts/', include('allauth.urls')),
    #path('logout', LogoutView.as_view()),
    path('', views.call_sevcik_template),
]
