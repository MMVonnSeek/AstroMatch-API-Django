from django.urls import path, include
from . import views_ui
from rest_framework.routers import DefaultRouter
from .views_api import SignViewSet

router = DefaultRouter()
router.register(r'signs', SignViewSet)

urlpatterns = [
    path('', views_ui.home_bonita, name='home-bonita'),
    path('signo/<int:sign_id>/', views_ui.sign_detail, name='sign-detail'),
    path('api/', include(router.urls)),
]
