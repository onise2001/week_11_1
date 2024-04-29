from django.urls import path
from .views import homepage, aboutpage, contactpage


urlpatterns = [
    path("home/", homepage),
    path("about/", aboutpage),
    path("contact/", contactpage),
]
