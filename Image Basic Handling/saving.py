import cv2
image = cv2.imread("img.png")

if image is not None:
    success = cv2.imwrite("output_python.png", image)
    if success:
        print("Image saved successfully as 'output_python.png'")
    else:
        print("Failedd to save an image")
else:
    print("Couldn't load the image")
