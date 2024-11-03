# Image Processing Pipeline in Python

This project implements a Python pipeline to process images stored in a specific folder. The pipeline resizes each image to a square format and applies padding when necessary. Processed images are saved in a uniquely generated folder each time the pipeline is run.

## Installation

1. Clone the repository.
2. Install dependencies with ``pip install -r requirements.txt``.
3. Set up PyCharm to [run main.py automatically](https://www.jetbrains.com/help/pycharm/run-debug-configuration.html#createExplicitly).

## Usage

To process images with this pipeline:

1. **Place your images** in the ``input_images/`` folder (or configure the path in ``main.py`` if using a different folder).
2. **Run the pipeline** by executing:

```python main.py```
3. **Find processed images** in a uniquely named subfolder inside the ``dataset/`` folder, created for each execution of the pipeline.
