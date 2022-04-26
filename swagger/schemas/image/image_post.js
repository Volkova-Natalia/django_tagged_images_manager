var schemas_image_post_request =
{
  "type": "object",
  "properties": {
    "content": { ...schemas_image.properties.content, ...{
      "description": "Image bytes",
    }},
    "metadata": schemas_image.properties.metadata
  }
}

var schemas_image_post_response =
{
  "type": "object",
  "properties": {
    "id": schemas_image.properties.id
  },
  "required": [
    "id"
  ]
}

