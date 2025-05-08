# Credential Reader
This repository contains the file for a credential image reader in python.

## Requirements
### 1. **Python version**
Python 3.6 or higher (recommended: Python 3.10+)

### 2. Packages and libraries
- **CV2**: a powerful library for working with images in Python.
- **EasyOCR**: a Python package for detecting and extracting text from images such as photos or scanned documents.
- **NumPy**: a powerful Python library primarily used for numerical computing, specially when working with arrays and matrices.
- **sys**: standard library module that provides access to system-specific parameters and functions.

You can install these libraries via `pip`: `pip install opencv-python easyocr numpy`

Because **sys** is part of Python's standard library, it does not require installation.

- ### System Dependencies for EasyOCR
  The package **EasyOCR** depends on PyTorch, so it must be installed as well:
  
  `pip install torch torchvision torchaudio`

### 3. Input files
For safety reasons, the Credentials used to test this code are not included in the repository. However, if you wish to test the code with your own custom credentials, 
you must first add them inside the code, in the *names* and *ids* arrays respectively. 

Please take into consideration:
- The names that are included in the *names* array and *ids* array must be all uppercase for the text detection to work properly.
- The image files to be used must be in the same folder in which the *main.py* file is located.
- Every name must have a matching ID with it. However, the order of the names and IDs in the arrays do not matter.

## Script execution
You must run the script from the terminal with the image file name as an argument:
`python main.py imageFileName.jpg`

Only one image file can be used with the main script at a time. If you wish to use more than than one image file, the complete command must be used again.

## Script functionality and description
The purpose of this script is to detect from image files containing credential photos if the detected data is part of previously stored data in the script. 
This is intended to serve as a simple simulation for identity confirmation when entering an authentication-restricted place, such as a university or a building.

This script uses the listed packages for image manipulation and text detection using an `ImageProcessing` function, where:
- Using CV2 to read image files and modify them in separate files, images are first converted into grayscale.
- Then, their atributes such as contrast and brightness are set to specific values and stored in a separate file.
- The newly-created file is then used to enhance its sharpness with a specified kernel (handled using NumPy), preparing the image for proper text detection.
- EasyOCR is now used to detect the characters from the previously modified image.
- The detected text is stored into a single uppercase string, and this text is returned by the function.

Furthermore, a `main` function is used to validate that the detected IDs and names match the stored data, where:
- The function makes sure that the user provides an image file name as a command-line argument (and will show an error message otherwise).
- If the previous condition is true, the function gets the image file name and processes it with `ImageProcessing` function to extract all detected text.
- It then uses list comprehension to validate if the detected ID is included in the stored ID list.
- If the ID matches, it then checks if there's a name that matches the respective ID. If any of this conditions aren't met, error messages will be shown.

Apart from function definitions, the script contains the necessary OCR reader initialization, the arrays for names and IDs, 
and a condition that validates that the `main` function is only executed if the script is executed from the terminal.

##Future improvements
Matching text validation currently only works through manually-added data in the respective arrays inside the script. Also, for text detection to work properly, names and IDs must be all set in uppercase. Aditionally, image files must be manually included in the project folder. As possible future improvements:
- The methods used to store data that will be validated can be reworked, where an actual MySQL database could be linked to the script, and queries could be used for data validation.
- A new image extraction method could be used, where the user would be allowed to type in the terminal (during code execution) a URL for an image that is stored in the web, which would then be used in the same way as local image files are currently used.
