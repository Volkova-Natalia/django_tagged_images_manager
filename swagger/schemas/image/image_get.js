var schemas_image_get_response =
{
  "type": "object",
  "properties": {
    "id": { ...schemas_image.properties.id, ...{
      "readOnly": true
    }},
    "content": { ...schemas_image.properties.content, ...{
      "description": "Image url",
      "readOnly": true,
      "format": "uri"
    }},
    "metadata": { ...schemas_image.properties.metadata, ...{
      "readOnly": true
    }},
    "created_date": { ...schemas_image.properties.created_date, ...{
      "readOnly": true
    }},
    "tags": { ...schemas_image.properties.tags, ...{
      "readOnly": true
    }},
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

