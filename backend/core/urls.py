from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, TeamMemberViewSet, ProjectViewSet, ContactViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'team', TeamMemberViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'contact', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 