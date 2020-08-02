from django.urls import path
from . import views

urlpatterns = [
    path('', views.coursesListView.as_view(), name='courses'),
    path('course-detail/<str:pk>', views.coursesDetailView.as_view(), name='course-detail'),
    path('course-add', views.coursesCreateView.as_view(), name='course-add'),
    path('course-update/<str:pk>', views.coursesUpdateView.as_view(), name='course-update'),
    path('course-delete/<str:pk>', views.coursesDeleteView.as_view(), name='course-delete'),
]