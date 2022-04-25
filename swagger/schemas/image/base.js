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
      "type": "string",
      "uniqueItems": false,
      "nullable": true
    },
    "created_date": {
      "type": "string",
      "uniqueItems": false,
      "nullable": false
    },
    "tags": {
      "type": "array",
      "items": {
        "value": {
          "type": "string",
          "uniqueItems": true,
          "nullable": false
        },
      }
    }
  }
}

