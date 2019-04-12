from django.conf.urls import url

from Charlie import views

# Template urls
app_name = 'Charlie'


urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^register/',views.register, name='register'),
]

