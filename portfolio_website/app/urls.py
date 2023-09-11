from django.urls import path
from .views import myprojectView, about, action, encrypted, decrypted


urlpatterns = [
    path("", myprojectView, name="home"),
    path("about/", about, name="about"),
    path("action/", action, name="action"),
    path("encrypted/", encrypted, name="encrypted"),
    path("decrypted/", decrypted, name="decrypted"),
]
