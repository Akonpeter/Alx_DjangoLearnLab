from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'Books', BookViewSet)


urlpatterns = [
    path("books/", BookList.as_view(), name="book_list_create"),
    path('api/', include(router.urls)),
]
