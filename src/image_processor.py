import os


class ImageProcessor:
    def __init__(self, image_folder: str):
        self.image_folder = image_folder
        if not os.path.isdir(self.image_folder):
            raise ValueError(
                f"The specified path '{self.image_folder}' is not a valid directory."
            )

    def process_folder(self):
        pass
