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
      "type": "string",
      "uniqueItems": false,
      "nullable": false
    },
    "images": {
      "type": "array",
      "items": schemas_image.properties.id
    }
  }
}

