from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BookModelViewset

router = DefaultRouter()
router.register('book', BookModelViewset, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]
