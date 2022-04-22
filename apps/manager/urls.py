from django.urls import path

from .views.image import ImagesView, ImageDetailsView
from .views.tag import TagsView, TagDetailsView
from .views.tag_of_image import TagsOfImageView, TagOfImageDetailsView


urlpatterns = [
    path('images/', ImagesView.as_view(), name='images'),  # GET, POST
    path('images/<int:image_id>', ImageDetailsView.as_view(), name='image-details'),  # GET, PUT, DELETE

    path('tags/', TagsView.as_view(), name='tags'),  # GET, POST
    path('tags/<str:tag_value>', TagDetailsView.as_view(), name='tag-details'),  # GET, PUT, DELETE

    path('images/<int:image_id>/tags/', TagsOfImageView.as_view(), name='tags-of-image'),  # POST
    path('images/<int:image_id>/tags/<str:tag_value>', TagOfImageDetailsView.as_view(), name='tag-of-image-details'),  # PUT, DELETE
]
