var responses_images_post_response_201 =
{
  "description": "Image created",
  "content": {
    "application/json;charset=utf-8": {
      "schema": schemas_image_post_response
    }
  }
}

var responses_images_post_response_400 =
{
  "description": "Invalid input",
  "content": {
    "application/json;charset=utf-8": {
      "examples": {
        "error_detail__content__required": examples_image_error_detail__content__required,
        "error_detail__metadata__required": examples_image_error_detail__metadata__required
      }
    }
  }
}

