from django.urls import path
from .views import home, contactus,thanks,contact,test
urlpatterns = [
    path('', home, name="home"),
    path('contact/', contactus, name="contactus"),
    path('contact1/', contact, name="contact1"),
    path('testimonial/', test, name="testimonial"),

    path('thanks/', thanks, name="thanks"),
]
