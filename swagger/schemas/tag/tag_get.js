var schemas_tag_get_response =
{
  "type": "object",
  "properties": {
    "value": schemas_tag.properties.value,
    "created_date": schemas_tag.properties.created_date,
    "images": schemas_tag.properties.images
  },
  "required": [
    "value",
    "created_date",
    "images"
  ]
}

var schemas_tags_get_response =
{
  "type": "array",
  "items": schemas_tag_get_response
}

