from rest_framework.routers import DefaultRouter

from django.urls import include, path

from blog.views import CatViewSet

router = DefaultRouter()

router.register('cats', CatViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
