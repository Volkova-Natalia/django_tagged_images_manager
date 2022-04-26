var schemas_tag_get_response =
{
  "title": "tag_get_response",
  "type": "object",
  "properties": {
    "value": { ...schemas_tag.properties.value, ...{
      "readOnly": true
    }},
    "created_date": { ...schemas_tag.properties.created_date, ...{
      "readOnly": true
    }},
    "images": { ...schemas_tag.properties.images, ...{
      "readOnly": true
    }}
  },
  "required": [
    "value",
    "created_date",
    "images"
  ]
}

var schemas_tags_get_response =
{
  "title": "tags_get_response",
  "type": "array",
  "items": schemas_tag_get_response
}

