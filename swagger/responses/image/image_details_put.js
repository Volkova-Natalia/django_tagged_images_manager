var responses_image_details_put_response_204 =
{
  "description": "Image updated",
  "content": {
    "application/json;charset=utf-8": {}
  }
}

var responses_image_details_put_response_400 =
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

