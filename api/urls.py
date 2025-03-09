from .views import MaintenanceDetailView, MaintenanceListView
from django.urls import path,re_path
from . import views


urlpatterns = [
    path('tasks/', MaintenanceListView.as_view(), name='task-list-create'),
    path('tasks/<int:id>/', MaintenanceDetailView.as_view(), name='task-detail'),
    path('tasks/<int:reg_no>/', MaintenanceDetailView.as_view(), name='reg-no-detail'),

]
