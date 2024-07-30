from django.urls import path
from .views import person_detail_html, person_form, person_list_html, profession_detail, profession_form, profession_list, person_detail, person_list, api_home, profession_list_html

urlpatterns = [
    path('', api_home, name='api_home'),
    path('profession_form/', profession_form, name='profession_form'),
    path('person_form/', person_form, name='person_form'),
    path('profession_list/', profession_list_html, name='profession_list'),
    path('person_list/', person_list_html, name='person_list'),
    path('person_detail/<int:pk>/', person_detail_html, name='person_detail'),

]