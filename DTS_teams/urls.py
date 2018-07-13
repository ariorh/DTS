from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from DTS_teams.models import Teams

urlpatterns = [
    path('', ListView.as_view(queryset=Teams.objects.all().order_by("region"),
                              template_name="DTS_teams/teams_main.html")),
    url('(?P<pk>\d+)',  DetailView.as_view(model=Teams, template_name="DTS_teams/team.html"))
]