from rest_framework import routers
from ems_app.viewsets import EmployeeViewset


router = routers.DefaultRouter()

router.register(r'employee', EmployeeViewset, basename="emp")
router.register(r'employee/<int:id>', EmployeeViewset, basename="emp_update")
urlpatterns = router.urls

