from rest_framework import routers
from .api import TeamViewSet, EmployeeViewSet

router = routers.DefaultRouter()
router.register("api/team", TeamViewSet, 'team')
router.register("api/employee", EmployeeViewSet, 'employee')
urlpatterns = router.urls
