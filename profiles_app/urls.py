from django.urls import path,include
from .views import HelloView,HelloViewset,UserProfileViewset,LoginViewset,ProfileFeedViewset

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('profiles', UserProfileViewset)
router.register('hello-viewset',HelloViewset,base_name='hello-viewset')
router.register('login', LoginViewset,base_name='login')
router.register('feed', ProfileFeedViewset)

urlpatterns = [
    path('helloview/',HelloView.as_view()),
    path('', include(router.urls))
]