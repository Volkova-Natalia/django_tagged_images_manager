var paths_tag_details =
{
  "get": {
    "tags": [
      "tags"
    ],
    "summary": "Get tag",
    "description": "tag_details",
    "parameters": [],
    "responses": {
      "200": responses_tag_details_get_response_200,
      "401": responses_response_401,
      "404": responses_response_404
    }
  },


  "put": {
    "tags": [
      "tags"
    ],
    "summary": "Update tag",
    "description": "tag_update",
    "parameters": [],
    "requestBody": request_bodies_tag_put_request,
    "responses": {
      "204": responses_tag_details_put_response_204,
      "400": responses_tag_details_put_response_400,
      "401": responses_response_401,
      "404": responses_response_404
    }
  },


  "delete": {
    "tags": [
      "tags"
    ],
    "summary": "Delete tag",
    "description": "tag_delete",
    "parameters": [],
    "responses": {
      "204": responses_tag_details_delete_response_204,
      "401": responses_response_401,
      "404": responses_response_404
    }
  }
}

