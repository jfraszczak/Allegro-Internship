from django.conf.urls import url
from GitHubAPI import views

urlpatterns = [
    url('repositories_list', views.repositories_list, name='repositories_list'),
    url('stars_count_sum', views.stars_count_sum, name='stars_count_sum')
]