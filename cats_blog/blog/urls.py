from django.urls import include, path

from rest_framework.routers import DefaultRouter

from blog.views import CatViewSet, UserViewSet

router = DefaultRouter()

router.register('cats', CatViewSet)
router.register('owners', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
