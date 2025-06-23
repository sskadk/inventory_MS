from django.contrib import admin
from django.urls import path
from ims.views import ProductTypeApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/types/', ProductTypeApiView.as_view({'get':'list', 'post':'create'})),
    path('product/types/<int:pk>/', ProductTypeApiView.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}))
]
