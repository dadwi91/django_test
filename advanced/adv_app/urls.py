from django.urls import path
from adv_app import views

#template tagging
app_name = 'adv_app'

urlpatterns = [
    path('',views.SchoolListView.as_view(),name='list'),
    path('<int:pk>/',views.SchoolDetailView.as_view(),name='detail'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.SchoolUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.SchoolDeleteView.as_view(),name='delete'),
]
