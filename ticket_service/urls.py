from django.urls import path, include
from rest_framework import routers

from ticket_service.views import TicketViewSet, ReservationViewSet, PerformanceViewSet

router = routers.DefaultRouter()

router.register("ticket", TicketViewSet)
router.register("reservation", ReservationViewSet)
router.register("performance", PerformanceViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "ticket_service"
