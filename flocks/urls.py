from django.urls import path, include
from flocks import views

urlpatterns =[
    path('',views.dashboard_view, name='dashboard_view'),
    path('records/', views.records_view, name='records_view'),
    path('farms/', views.farms_view, name='farms_view'),
    path('flocks/', views.flocks_view, name='flocks_view'),
    path('flocks-list/<str:farm>', views.flocks_list, name='flocks-list'),
    path('houses/', views.houses_view, name='houses_view'),
    path('owners/', views.owners_view, name='owners_view'),
    path('settings/', views.settings_view, name='settings_view'),
    path('vaccinations/', views.vaccinations_view, name='vaccinations_view'),

]