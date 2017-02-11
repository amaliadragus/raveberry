from django.conf.urls import url, include
from rest_framework import routers
from closet.api import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'items', views.ItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^collections/', include('rest_framework.urls', namespace='rest_framework'))
]