from rest_framework import routers
from .api import RefugeViewSet, AnimalViewSet, EmployeeViewSet

router = routers.DefaultRouter()
router.register('api/refuges', RefugeViewSet, 'refuges')
router.register('api/animals', AnimalViewSet, 'animals')
router.register('api/employees', EmployeeViewSet, 'employees')

urlpatterns = router.urls
