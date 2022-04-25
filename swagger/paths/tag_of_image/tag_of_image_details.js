var paths_tag_of_image_details =
{
  "put": {
    "tags": [
      "tags_of_image"
    ],
    "summary": "Update tag_of_image",
    "description": "tag_of_image_update",
    "parameters": [],
    "requestBody": request_bodies_tag_of_image_put_request,
    "responses": {
      "204": responses_tag_of_image_details_put_response_204,
      "400": responses_tag_of_image_details_put_response_400,
      "401": responses_response_401,
      "404": responses_response_404
    }
  },


  "delete": {
    "tags": [
      "tags_of_image"
    ],
    "summary": "Delete tag_of_image",
    "description": "tag_of_image_delete",
    "parameters": [],
    "responses": {
      "200": responses_tag_of_image_details_delete_response_204,
      "401": responses_response_401,
      "404": responses_response_404
    }
  }
}

