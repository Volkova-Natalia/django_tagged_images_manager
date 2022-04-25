var paths_image_details =
{
  "get": {
    "tags": [
      "images"
    ],
    "summary": "Get image",
    "description": "image_details",
    "parameters": [],
    "responses": {
      "200": responses_image_details_get_response_200,
      "401": responses_response_401,
      "404": responses_response_404
    }
  },


  "put": {
    "tags": [
      "images"
    ],
    "summary": "Update image",
    "description": "image_update",
    "parameters": [],
    "requestBody": request_bodies_image_put_request,
    "responses": {
      "204": responses_image_details_put_response_204,
      "400": responses_image_details_put_response_400,
      "401": responses_response_401,
      "404": responses_response_404
    }
  },


  "delete": {
    "tags": [
      "images"
    ],
    "summary": "Delete image",
    "description": "image_delete",
    "parameters": [],
    "responses": {
      "204": responses_image_details_delete_response_204,
      "401": responses_response_401,
      "404": responses_response_404
    }
  }
}

