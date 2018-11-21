from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.index,name = 'home'),
    url(r'^profile/',views.profile, name='profile'),
    url(r'^search_results/',views.search_results,name='search_results'),
    url(r'^project/(\d+)/$', views.single_project, name='project'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)