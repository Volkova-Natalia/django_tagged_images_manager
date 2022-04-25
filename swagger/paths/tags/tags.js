var paths_tags =
{
  "get": {
    "tags": [
      "tags"
    ],
    "summary": "Get tags",
    "description": "tags",
    "parameters": [],
    "responses": {
      "200": responses_tags_get_response_200,
      "401": responses_response_401
    }
  },


  "post": {
    "tags": [
      "tags"
    ],
    "summary": "Create tag",
    "description": "tag_create",
    "parameters": [],
    "requestBody": request_bodies_tag_post_request,
    "responses": {
      "201": responses_tags_post_response_201,
      "400": responses_tags_post_response_400,
      "401": responses_response_401
    }
  }
}
