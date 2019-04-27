from django.conf.urls import url
#from django.contrib.auth.views import login
from . import views
from django.urls import path

app_name='account'
urlpatterns = [
path('', views.home),
path('loginL/',views.login_L,name='login_L'),
path('signupL/',views.signup_L,name='signup_L'),
path('signupE/',views.signup_E,name='signup_E'),
path('loginE/',views.login_E,name='login_E'),
path('signupL/detL/',views.detL,name='detL'),
path('signupE/detE/',views.detE,name='detE'),
path('loginE/dashE/',views.dashE,name='dashE'),
path('loginL/dashL/',views.dashL,name='dashL'),
path('loginE/dashE/find/<name>',views.find,name='find'),
path('feed/', views.FeedViewSet),
path('save/', views.saveData),
]
