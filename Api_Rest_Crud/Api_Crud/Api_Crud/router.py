from Api_Employer.views import ApiEmployerView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Api_Employer', ApiEmployerView)