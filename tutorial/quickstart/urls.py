#from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart.views import*

router = routers.DefaultRouter()
router.register(r'post', PostView)
router.register(r'comment', CommentView)
router.register(r'category', CategoryView)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = router.urls