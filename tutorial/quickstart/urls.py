from rest_framework import routers

from tutorial.quickstart.views import *

router = routers.DefaultRouter()
router.register(r'post', PostView)
router.register(r'comment', CommentView)
router.register(r'category', CategoryView)


urlpatterns = router.urls