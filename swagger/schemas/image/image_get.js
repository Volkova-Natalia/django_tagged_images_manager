var schemas_image_get_response =
{
  "type": "object",
  "properties": {
    "id": schemas_image.properties.id,
    "content": schemas_image.properties.content,
    "metadata": schemas_image.properties.metadata,
    "created_date": schemas_image.properties.created_date,
    "tags": schemas_image.properties.tags,
  },
  "required": [
    "id",
    "content",
    "metadata",
    "created_date",
    "tags"
  ]
}


var schemas_images_get_response =
{
  "type": "array",
  "items": schemas_image_get_response
}

