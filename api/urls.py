from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_home),
    path("simulate/", views.simulate),
    path("optimize/", views.optimize),
    path("report/", views.download_pdf, name="report"),
    path('register/', views.register),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
]