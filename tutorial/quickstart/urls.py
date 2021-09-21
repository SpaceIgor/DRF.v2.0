from rest_framework import routers
from tutorial.quickstart.views import *
from django.views.decorators.cache import cache_page

router = routers.DefaultRouter()
cache_page(100)(router.register(r'post', PostView))
cache_page(100)(router.register(r'comment', CommentView))
cache_page(100)(router.register(r'category', CategoryView))


urlpatterns = router.urls

rns = router.urls