import cv2
img = cv2.imread("img.png")
if img is None:
    print("Error: Image is not loaded")
else:
    print("Image is loaded successfully")
