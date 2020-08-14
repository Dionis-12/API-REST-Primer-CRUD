from employers.views import EmployersView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employers', EmployersView)