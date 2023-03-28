from django.urls import path
from . import views

urlpatterns = [
    path('app', views.CrudList.as_view(), name='crud_list'),
    path('app/<int:pk>', views.CrudDetail.as_view(), name='crud_detail')
]