# Assignment 2: Drawing Shapes and Text on an Image using OpenCV
# This script allows the user to draw a line, rectangle, circle, or text on an
import cv2
import numpy as np

image_location = input("Enter the location of the image :\n")

print("The location of image is given by you\n", image_location)

image = cv2.imread(image_location)

if image is not None:
    user_option = int(input("What do you want to draw on image:\n"
                            "Press 1 for line\n"
                            "Press 2 for rectangle\n"
                            "Press 3 for circle\n"
                            "Press 4 for text\n"))

    if user_option == 1:
        # Line
        x1, y1 = np.fromstring(input("Enter x1 and y1 of point 1:\n"), sep=' ', dtype=int)
        x2, y2 = np.fromstring(input("Enter x2 and y2 of point 2:\n"), sep=' ', dtype=int)
        color = tuple(map(int, input("Enter BGR color values separated by space:\n").split()))
        thickness = int(input("Enter thickness of line:\n"))

        cv2.line(image, (x1, y1), (x2, y2), color, thickness)
        cv2.imshow("Image with Line", image)
        cv2.imwrite("output_image_with_line.jpg", image)

    elif user_option == 2:
        # Rectangle
        x1, y1 = np.fromstring(input("Enter x1 and y1 of point 1:\n"), sep=' ', dtype=int)
        x2, y2 = np.fromstring(input("Enter x2 and y2 of point 2:\n"), sep=' ', dtype=int)
        color = tuple(map(int, input("Enter BGR color values separated by space:\n").split()))
        thickness = int(input("Enter thickness of line:\n"))

        cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)
        cv2.imshow("Image with Rectangle", image)
        cv2.imwrite("output_image_with_rectangle.jpg", image)

    elif user_option == 3:
        # Circle
        x1, y1 = np.fromstring(input("Enter x1 and y1 of center point:\n"), sep=' ', dtype=int)
        radius = int(input("Enter radius of circle:\n"))
        color = tuple(map(int, input("Enter BGR color values separated by space:\n").split()))
        thickness = int(input("Enter thickness of circle border:\n"))

        cv2.circle(image, (x1, y1), radius, color, thickness)
        cv2.imshow("Image with Circle", image)
        cv2.imwrite("output_image_with_circle.jpg", image)

    elif user_option == 4:
        # Text
        x1, y1 = np.fromstring(input("Enter x1 and y1 of starting point:\n"), sep=' ', dtype=int)
        text = input("Enter the text:\n")
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = float(input("Enter font scale:\n"))
        color = tuple(map(int, input("Enter BGR color values separated by space:\n").split()))
        thickness = int(input("Enter thickness:\n"))

        cv2.putText(image, text, (x1, y1), font, font_scale, color, thickness)
        cv2.imshow("Image with Text", image)
        cv2.imwrite("output_image_with_text.jpg", image)

    else:
        print("Invalid option")
        exit()

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Sorry! Image is not loaded. Try Again.")
