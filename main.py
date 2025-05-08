import cv2
import easyocr
import numpy as np
import sys


# Function for image processing.
def imageProcessing(fileName):
    # Read image.
    img = cv2.imread(fileName)
    # Convert the image to grayscale.
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Alpha is used for contrast, while beta is used for brightness.
    imgContrast = cv2.convertScaleAbs(imgGray, 
                                      alpha=1.75, 
                                      beta=-300)
    
    # Store the modified image
    cv2.imwrite(f"{fileName}_contrast.png", imgContrast)
    
    # A sharpening filter kernel, enhances edges, makes text clearer.
    kernel = np.array([[-1,-1,-1],
                      [-1,9,-1],
                      [-1,-1,-1]])
    
    # Apply the sharpening filter to the contrast-enhanced image.
    imgSharpness = cv2.filter2D(imgContrast,-1,kernel)
    
    # Store the newly modified image
    cv2.imwrite(f"{fileName}_sharpness.png", imgSharpness)

    # Use easyocr to detect characters in images.
    # If 'detail=0', then only the text is returned.
    results = reader.readtext(imgSharpness, detail=0)
    
    #Join all OCR-detected strings into one big uppercase string.
    detectedText = " ".join(results).upper()
    return detectedText


# Function to be executed if the script is run from the command line
def main():
    # Check if user provides an image file name as a command-line argument.
    if len(sys.argv)<2:
        print("Error. Try using: python main.py imageFileName.jpg")
        return
    
    # Get the image file name and extract all detected text with function.
    file = sys.argv[1]
    result = imageProcessing(file)
    
    # Name and ID filtering using list comprehension
    idApproved = [id for id in ids if 
                        id in result]
    if idApproved:
        # If the ID is successfully read, check the student's name 
        nameApproved = [name for name in names if name in result]
        if nameApproved:
            print(f"Success. Welcome: {nameApproved[0]}.")
        else:
            print("Failed. The name for the ID does not match.")
    else:
        print("Failed. The ID does not match.")


# Initialize ocr reader in spanish.
reader = easyocr.Reader(['es'])

# Arrays for accepted names and IDs.
names = ["OCTAVIO SEBASTIÁN HERNÁNDEZ GALINDO", "GAEL CASTILLO ZEPEDA"]
ids = ["A01638638", "A01638993"]

# Run main() only when the script is executed directly.
if __name__ == "__main__":
    main()