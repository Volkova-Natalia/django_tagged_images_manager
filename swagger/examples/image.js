var examples_image_get_response =
{
  "image_get_response": {
    "value": {
      "id": 4,
      "content": "http://testserver/media/images/apps/manager/tests/976f5467-7c65-4193-8cb5-e4f9888be14b-test_0.png",
      "metadata": "{'Filename': 'apps/manager/tests/test_0.png', 'ImageSize': [22, 23], 'ImageHeight': 23, 'ImageWidth': 22, 'ImageFormat': 'PNG', 'ImageMode': 'RGBA', 'IsImageAnimated': false, 'FramesInImage': 1, 'exif': {}}",
      "created_date": "2022-04-25T12:31:07.820251Z",
      "tags": ["tag_0"]
    }
  }
}

var examples_images_get_response =
{
  "images_get_response": {
    "value": [examples_image_get_response.image_get_response.value]
  }
}

var examples_images_post_request_body =
{
  "images_post_request_body": {
    "value": {
      "metadata": "{'Filename': 'apps/manager/tests/test_1.png', 'ImageSize': [22, 23], 'ImageHeight': 23, 'ImageWidth': 22,'ImageFormat': 'PNG', 'ImageMode': 'RGBA', 'IsImageAnimated': false, 'FramesInImage': 1, 'exif': {}}",
      "content": "iVBORw0KGgoAAAANSUhEUgAAABYAAAAXCAYAAAAP6L+eAAAAfElEQVR4nO2VPRIAEQyFY8eNXECbE2tdwJmy1RYrPxhrq7wOyed5wwhERHBA1wmogx0sK/YTGRvUksymjO01lupFx32jtFZLMg0w8MjtbI2accbGnM/ENATv6l+wdNyVGFSwtcEn4EfW9dPEHogGXHWvgndiAAAI/jUdB9/j4Sl/z/X9xAAAAABJRU5ErkJggg=="
    }
  }
}

var examples_image_put_request_body =
{
  "image_put_request_body": {
    "value": {
      "metadata": "{'Filename': 'apps/manager/tests/test_1.png', 'ImageSize': [22, 23], 'ImageHeight': 23, 'ImageWidth': 22,'ImageFormat': 'PNG', 'ImageMode': 'RGBA', 'IsImageAnimated': false, 'FramesInImage': 1, 'exif': {}}",
      "content": "iVBORw0KGgoAAAANSUhEUgAAABYAAAAXCAYAAAAP6L+eAAAAfElEQVR4nO2VPRIAEQyFY8eNXECbE2tdwJmy1RYrPxhrq7wOyed5wwhERHBA1wmogx0sK/YTGRvUksymjO01lupFx32jtFZLMg0w8MjtbI2accbGnM/ENATv6l+wdNyVGFSwtcEn4EfW9dPEHogGXHWvgndiAAAI/jUdB9/j4Sl/z/X9xAAAAABJRU5ErkJggg=="
    }
  }
}



var examples_image_error_detail__content__required =
{
  "value": {
    "content": "[ErrorDetail(string='This field is required.', code='required')]"
  }
}

var examples_image_error_detail__metadata__required =
{
  "value": {
    "metadata": "[ErrorDetail(string='This field is required.', code='required')]"
  }
}

