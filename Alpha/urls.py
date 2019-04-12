from django.conf.urls import url

from Alpha import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^stories/', views.stories, name='stories')
]