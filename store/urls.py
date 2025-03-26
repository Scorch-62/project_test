from django.urls import path
import apps
import views

store_name = apps.StoreConfig.name

urlpatterns = [
    path('', views.home, name='home')
]
