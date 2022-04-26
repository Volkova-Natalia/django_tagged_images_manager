var schemas_image_put_request =
{
  "type": "object",
  "properties": {
    "content": { ...schemas_image.properties.content, ...{
      "description": "Image bytes",
    }},
    "metadata": schemas_image.properties.metadata
  }
}

