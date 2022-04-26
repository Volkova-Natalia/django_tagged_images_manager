var schemas_image =
{
  "type": "object",
  "properties": {
    "id": {
      "type": "number",
      "uniqueItems": true,
      "nullable": false
    },
    "content": {
      "type": "string",
      "uniqueItems": true,
      "nullable": false
    },
    "metadata": {
      "description": "Metadata of the image",
      "type": "string",
      "uniqueItems": false,
      "nullable": true
    },
    "created_date": {
      "description": "Created date of the image",
      "type": "string",
      "format": "date-time",
      "uniqueItems": false,
      "nullable": false
    },
    "tags": {
      "title": "tags",
      "description": "Tags for the image",
      "type": "array",
      "items": {
        "description": "Tag value",
        "type": "string",
        "uniqueItems": true,
        "nullable": false
      }
    }
  }
}

