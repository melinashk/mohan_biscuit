from django.urls import path
from .views import *

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('aboutus', AboutView.as_view(), name='aboutus'),
    path('contact', ContactView.as_view(), name='contact'),
    path('product', ProductView.as_view(), name='product'),
    path('rating', register, name='rating'),
    path('ratepage', ratepage, name='ratepage'),
    path('careerstatus', StatusView.as_view(), name='careerstatus'),
    path('career', career, name='career'),
    path('inquiry', inquiry, name='inquiry'),
]