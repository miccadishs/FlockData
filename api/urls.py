from django.urls import path
from api import views

urlpatterns = [
    path('site_list/', views.site_list, name='site_list'),
    path('breed_list/', views.breed_list, name='breed_list'),
    path('breed_type_list/', views.breed_type_list, name='breed_type_list'),
    path('owner_list/', views.owner_list, name='owner_list'),
    path('country_list/', views.country_list, name='country_list'),
    path('farm_list/<str:uid>', views.farm_list, name='farm_list'),
    path('flock_list/', views.flock_list, name='flock_list'),
    path('house_list/', views.house_list, name='house_list'),
    path('record_list/', views.record_list, name='record_list'),
    path('record_create/', views.record_create, name='record_create'),
    path('target_list/', views.target_list, name='target_list'),
    path('vaccine_list/', views.vaccine_list, name='vaccine_list'),
    path('vaccination_list/', views.vaccination_list, name='vaccination_list'),
    path('target_details_list/', views.target_details_list, name='target_details_list'),
    path('adjustment_create/', views.adjustment_create, name="adjustment_create"),
    path('adjustment_list/', views.adjustment_list, name='adjustment_list'),

]
