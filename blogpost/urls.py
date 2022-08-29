from django.urls import path
from .views import ApexDataView, BlogCreate,BlogList, BlogDetail,BlogDelete,BlogUpdate,TopView

urlpatterns = [
    path('list/', BlogList.as_view(), name='list'),
    path('detail/<int:pk>/', BlogDetail.as_view(),name='detail'),
    path('create/', BlogCreate.as_view(), name='create'),
    path('delete/<int:pk>', BlogDelete.as_view(), name ='delete'),
    path('update/<int:pk>', BlogUpdate.as_view(), name = 'update'),
    path('top/', TopView.as_view(), name='top'),
    path('apex_data/', ApexDataView.as_view(), name='apex_data'),
    ]