from rest_framework import routers
from .views import BookViewSet

app_name = "books"

router = routers.DefaultRouter()

router.register(r"", BookViewSet, basename="book")

urlpatterns = router.urls
