import cv2
import pytesseract as ocr
from PIL import Image
import numpy as np
import streamlit as st
import os 

os.environ.get('PORT', 8501)

st.title("Text Extraction Application")
st.subheader("upload your image bellow please")

uploaded_file = st.file_uploader("Choose an image...", type=['png','jpg','jpeg'])

if uploaded_file is not None:
       # Convert the uploaded file to an OpenCV image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    # Step 1: Display the uploaded image
    st.image(img, channels="BGR", caption="Uploaded Image")

    # Step 2: Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Step 3: Apply Otsu's Binarization
    _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Step 4: Perform OCR
    pil_image = Image.fromarray(thresholded)
    text = ocr.image_to_string(pil_image, config='--psm 11').strip()

    # Step 5: Display extracted text
    st.subheader("Extracted Text")
    if text:
        st.write(text)
    else:
        st.write("No text detected.")