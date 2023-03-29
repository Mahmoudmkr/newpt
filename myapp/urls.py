from django.urls import path
from . import views

urlpatterns=[
    path('',views.ProjectLitView.as_view(), name='list'),
    path('project/create',views.ProjectCreateView.as_view(), name='create'),
    path('project/edit/<int:pk>',views.ProjectUpdateView.as_view(), name='update'),

]