import os
from datetime import datetime
from PIL import Image


class ImageProcessor:
    PADDING_COLOR = (114, 114, 144)
    DATETIME_FORMAT = "%Y%m%d%H%M%S"
    OUTPUT_FOLDER = "datasets"

    def __init__(self, folder_path: str):
        """
        Sets the input folder path and creates a timestamped output folder for processed images.

        Parameters:
        -----------
        folder_path : str
            Path to the folder containing images to process.
        """
        self.folder_path = folder_path
        self.output_folder = os.path.join(
            self.OUTPUT_FOLDER, datetime.now().strftime(self.DATETIME_FORMAT)
        )
        os.makedirs(self.output_folder, exist_ok=True)

    def process_folder(self, size: int):
        """
        Processes all .jpg files in the folder to a max dimension, adding padding if needed.

        Parameters:
        -----------
        size : int
            Maximum dimension for the longer side of each image.
        """
        for filename in os.listdir(self.folder_path):
            if filename.lower().endswith(".jpg"):
                self.process_image(filename, size)

    def process_image(self, filename: str, size: int):
        """
        Resizes and adds padding to an image, saving it to the output folder.

        Parameters:
        -----------
        filename : str
            Name of the image file to process.
        size : int
            Maximum dimension for resizing.
        """
        img_path = os.path.join(self.folder_path, filename)
        with Image.open(img_path) as img:
            img = self.resize_image(img, size)
            img = self.add_padding(img)
            output_path = os.path.join(self.output_folder, filename)
            img.save(output_path)

    def resize_image(self, img: Image.Image, size: int) -> Image.Image:
        """
        Resizes an image while maintaining its aspect ratio.

        Parameters:
        -----------
        img : Image.Image
            Image to resize.
        size : int
            Maximum dimension for the longest side.

        Returns:
        --------
        Image.Image
            Resized image.
        """
        width, height = img.size
        aspect_ratio = min(size / width, size / height)
        new_width = int(width * aspect_ratio)
        new_height = int(height * aspect_ratio)

        return img.resize((new_width, new_height), Image.LANCZOS)

    def add_padding(self, img: Image.Image) -> Image.Image:
        """
        Adds padding to make an image square if it’s not already.

        Parameters:
        -----------
        img : Image.Image
            Image to add padding to.

        Returns:
        --------
        Image.Image
            Square image with padding if needed.
        """
        width, height = img.size
        if width == height:
            return img
        elif width > height:
            new_img = Image.new("RGB", (width, width), self.PADDING_COLOR)
            new_img.paste(img, (0, (width - height) // 2))
        else:
            new_img = Image.new("RGB", (height, height), self.PADDING_COLOR)
            new_img.paste(img, ((height - width) // 2, 0))

        return new_img
