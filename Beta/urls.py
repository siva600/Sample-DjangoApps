from django.conf.urls import url, include
from Beta import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='beta'),
    url(r'^beta/', views.index, name='beta_index'),
    url(r'^help/', views.help, name='help'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls))

    ] + urlpatterns


