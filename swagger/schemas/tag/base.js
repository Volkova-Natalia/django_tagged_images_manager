var schemas_tag =
{
  "type": "object",
  "properties": {
    "value": {
      "type": "string",
      "uniqueItems": true,
      "nullable": false
    },
    "created_date": {
      "description": "Created date of the tag",
      "type": "string",
      "format": "date-time",
      "uniqueItems": false,
      "nullable": false
    },
    "images": {
      "type": "array",
      "items": schemas_image.properties.id
    }
  }
}

