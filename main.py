from src.image_processor import ImageProcessor


def main():
    folder_path = "input_images"
    size = 640
    processor = ImageProcessor(folder_path)
    processor.process_folder(size)


if __name__ == "__main__":
    main()
