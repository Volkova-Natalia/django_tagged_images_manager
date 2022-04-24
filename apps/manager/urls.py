from rest_framework import routers
from django.urls import path

from .views import (
    ImagesView, TagsView,
    TagsOfImageView, TagOfImageDetailsView,
)


router = routers.SimpleRouter()
router.register(r'images', ImagesView)
router.register(r'tags', TagsView)
urlpatterns = (
        router.urls +
        [
            path('images/<int:image_id>/tags/', TagsOfImageView.as_view(), name='tag-of-image'),  # POST
            path('images/<int:image_id>/tags/<str:tag_value>', TagOfImageDetailsView.as_view(), name='tag-of-image-detail'),  # PUT, DELETE
        ]
)
