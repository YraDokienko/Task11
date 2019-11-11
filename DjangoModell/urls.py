from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_choice),
    path('view/', views.ModelView.as_view()),
    path('list/', views.ModelsViewList.as_view()),
    path('template/', views.ModelViewTemplate.as_view()),
]