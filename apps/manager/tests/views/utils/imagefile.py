from typing import Optional
import base64
from io import BytesIO
import json

from PIL import Image as PILImage
from PIL.ExifTags import TAGS


class ImageWithMetadata:
    __slots__ = ('content', 'content_raw', 'metadata', 'data')

    def __init__(self, filename: Optional[str] = 'test_0.jpg'):
        self.content = None
        self.content_raw = None
        self.metadata = None
        self.data = None
        self.make_data()
        self.create(filename=filename)

    def make_data(self):
        self.data = {
            'content': self.content,
            'metadata': self.metadata,
        }

    def create(self, filename: Optional[str] = 'test_0.jpg'):
        try:
            img = PILImage.open(filename)
        except:
            return
        else:
            info_dict = {
                'Filename': img.filename,
                'ImageSize': img.size,
                'ImageHeight': img.height,
                'ImageWidth': img.width,
                'ImageFormat': img.format,
                'ImageMode': img.mode,
                'IsImageAnimated': getattr(img, "is_animated", False),
                'FramesInImage': getattr(img, "n_frames", 1),
                'exif': {},
            }
            exifdata = img.getexif()
            for tag_id in exifdata:
                # get the tag name, instead of human unreadable tag id
                tag = TAGS.get(tag_id, tag_id)
                data = exifdata.get(tag_id)
                if isinstance(data, bytes):
                    data = data.decode()
                info_dict['exif'][tag] = data

            self.metadata = json.dumps(info_dict)

            buffered = BytesIO()
            img.save(buffered, format=info_dict['ImageFormat'])
            img_byte: bytes = buffered.getvalue()
            self.content_raw = img_byte
            img_base64 = base64.b64encode(img_byte)
            img_str: str = img_base64.decode('utf-8')
            self.content = img_str
            self.make_data()
