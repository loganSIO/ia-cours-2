import os
from datetime import datetime
from PIL import Image


class ImageProcessor:
    def __init__(self, folder_path: str):
        self.folder_path = folder_path
        self.output_folder = os.path.join(
            "datasets", datetime.now().strftime("%Y%m%d%H%M%S")
        )
        os.makedirs(self.output_folder, exist_ok=True)

    def process_folder(self, size: int):
        for filename in os.listdir(self.folder_path):
            if filename.lower().endswith((".jpg",)):
                self.process_image(filename, size)

    def process_image(self, filename: str, size: int):
        img_path = os.path.join(self.folder_path, filename)
        with Image.open(img_path) as img:
            img = self.resize_image(img, size)
            img = self.add_padding(img)
            output_path = os.path.join(self.output_folder, filename)
            img.save(output_path)

    def resize_image(self, img: Image.Image, size: int) -> Image.Image:
        width, height = img.size
        aspect_ratio = min(size / width, size / height)
        new_width = int(width * aspect_ratio)
        new_height = int(height * aspect_ratio)

        img.resize((new_width, new_height), Image.LANCZOS)

        return img

    def add_padding(self, img: Image.Image) -> Image.Image:
        background_color = (114, 114, 144)
        width, height = img.size
        if width == height:
            return img
        elif width > height:
            new_img = Image.new("RGB", (width, width), background_color)
            new_img.paste(img, (0, (width - height) // 2))
            return new_img
        else:
            new_img = Image.new("RGB", (height, height), background_color)
            new_img.paste(img, ((height - width) // 2, 0))
            return new_img
