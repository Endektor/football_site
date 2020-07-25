"""the_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import: from my_app import views
    2. Add a URL to urlpatterns: path('', views.home, name='home')
Class-based views
    1. Add an import: from other_app.views import Home
    2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backend import views
from django.conf.urls import url

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/posts/$', views.posts_list),
    url(r'^api/posts/(?P<id>[0-9]+)$', views.posts_detail),
    url(r'^api/players/$', views.players_list),
    url(r'^api/players/(?P<id>[0-9]+)$', views.players_detail),
    url(r'^api/teams/$', views.teams_list),
    url(r'^api/teams/(?P<id>[0-9]+)$', views.teams_detail),
    url(r'^api/tournaments/$', views.tournaments_list),
    url(r'^api/tournaments/(?P<id>[0-9]+)$', views.tournaments_detail),
    url(r'^api/memberships/$', views.memberships_list),
    url(r'^api/memberships/(?P<id>[0-9]+)$', views.memberships_detail),
    url(r'^api/matches/$', views.matches_list),
    url(r'^api/matches/(?P<id>[0-9]+)$', views.matches_detail),
    url(r'^api/slides/$', views.slides_list),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns.append(url(r'^', views.ReactAppView.as_view()))