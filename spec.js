var spec =

{
  "openapi": "3.0.0",
  "info": {
    "title": "tagged_images_manager",
    "version": "v0"
  },
  "servers": [
    {
      "url": "manager"
    }
  ],

  "tags": [
    {
      "name": "images"
    },
    {
      "name": "tags"
    },
    {
      "name": "tags_of_image"
    }
  ],



  "paths": {
    "/images/": paths_images,
    "/images/<int:image-id>": paths_image_details,

    "/tags/": paths_tags,
    "/tags/<str:tag-value>": paths_tag_details,

    "/images/<int:image-id>/tags/": paths_tags_of_image,
    "/images/<int:image-id>/tags/<str:tag-value>": paths_tag_of_image_details
  }


}

