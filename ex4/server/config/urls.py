from django.contrib import admin
from django.urls import path, include
from main.views import ProductsView,PurchasedView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Products/', ProductsView.as_view(), name='Products'),
    path('Purchased/', PurchasedView.as_view(), name='Purchased'),
]