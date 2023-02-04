from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('examimage', views.ExamImageViewSet, basename='examimage')



examimage_router = routers.NestedSimpleRouter(
    router, 'examimage', lookup='examimage')



# URLConf
urlpatterns = router.urls + examimage_router.urls
