from rest_framework import routers
from .views import PageViewSet

app_name = "pages"

router = routers.DefaultRouter()

router.register(r'books/(?P<book_id>\d+)/pages', PageViewSet, basename='page')

urlpatterns = router.urls
