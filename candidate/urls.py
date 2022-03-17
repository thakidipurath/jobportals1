from candidate import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('candidate/register',views.CandidateViewSet,basename="candidateprofile"),
router.register('job/list',views.CandidateViewSet,basename="candidateprofile"),

urlpatterns=[

]+router.urls
