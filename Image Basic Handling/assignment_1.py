import cv2

image_location = input("Enter the full path of the image:\n")
print("You entered:", image_location)

image = cv2.imread(image_location)

if image is not None:
    print("Image loaded successfully!")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow("Gray Scale image", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Gray Scale image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    filename = input("Enter the name of gray image to save:\n")
    success = cv2.imwrite(f"{filename}.png", gray)

    if success:
        print("Image saved successfully.")
    else:
        print("Image could not be saved.")
else:
    print("Image not loaded! Enter correct path.")
