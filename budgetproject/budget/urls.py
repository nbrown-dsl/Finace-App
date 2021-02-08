from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.project_list,name='project_list'),
    path('add', views.ViewBudgets.as_view(),name='add'),
    path('project_detail/<projectId>',views.project_detail,name="project_detail")
    # path('<slug:project_slug>',views.project_detail,name="detail")#generally using data already obtained. For instance, a slug uses the title of an article to generate a URL.
]
