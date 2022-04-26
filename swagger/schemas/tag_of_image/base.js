var schemas_tag_of_image =
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
      "title": "images",
      "description": "Images which have the tag",
      "type": "array",
      "items": {
        "description": "Image id",
        "type": "number",
        "uniqueItems": true,
        "nullable": false
      }
    }
  }
}

