from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, TeamMemberViewSet, ProjectViewSet, ContactViewSet, VoiceWorkViewSet, OrderViewSet, PaymentTransactionViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'team-members', TeamMemberViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'voice-works', VoiceWorkViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'payment', PaymentTransactionViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
] 