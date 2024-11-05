from src.image_processor import ImageProcessor


def main():
    DEFAULT_INPUT_FOLDER = "input_images"
    DEFAULT_SIZE = 640
    folder_path = DEFAULT_INPUT_FOLDER
    size = DEFAULT_SIZE
    processor = ImageProcessor(folder_path)
    processor.process_folder(size)


if __name__ == "__main__":
    main()
