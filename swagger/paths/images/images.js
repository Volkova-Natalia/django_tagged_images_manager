var paths_images =
{
  "get": {
    "tags": [
      "images"
    ],
    "summary": "Get images",
    "description": "images",
    "parameters": [],
    "responses": {
      "200": responses_images_get_response_200,
      "401": responses_response_401
    }
  },


  "post": {
    "tags": [
      "images"
    ],
    "summary": "Create image",
    "description": "image_create",
    "parameters": [],
    "requestBody": request_bodies_image_post_request,
    "responses": {
      "201": responses_images_post_response_201,
      "400": responses_images_post_response_400,
      "401": responses_response_401
    }
  }
}
