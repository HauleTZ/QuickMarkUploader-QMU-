import cv2
import pytesseract

def detected_text(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply OCR to extract the text from the image
    text = pytesseract.image_to_string(gray)

    # Print the extracted text
    return text
