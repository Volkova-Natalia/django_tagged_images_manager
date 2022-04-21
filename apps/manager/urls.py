from django.urls import path

from .views.image import ImagesView, ImageDetailsView
from .views.tag import TagsView, TagDetailsView


urlpatterns = [
    path('images/', ImagesView.as_view()),  # GET, POST
    path('images/<int:image_id>', ImageDetailsView.as_view()),  # GET, PUT, DELETE

    path('tags/', TagsView.as_view()),  # GET, POST
    path('tags/<str:tag_value>', TagDetailsView.as_view()),  # GET, PUT, DELETE
]
