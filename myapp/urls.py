from django.urls import path
from . import views
urlpatterns = [
    path('', views.homeView, name='home'),
    path('geography', views.geographyView, name='geography'),
    path('last_vacs', views.latest_vacancies_view, name='last_vacs'),
    path('demand', views.demandView, name='demand'),
    path('skills', views.skillsView, name='skills'),
]
