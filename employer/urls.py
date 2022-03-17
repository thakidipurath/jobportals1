from employer import views
from django.urls import path
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('employer/register',views.EmployerRegisterView,basename="employerregister"),
router.register('employer/job',views.JobView,basename="employerjoblist"),


urlpatterns=[
    #path('user/create/',views.UserCreationView.as_view(),name="usercreate")

]+router.urls