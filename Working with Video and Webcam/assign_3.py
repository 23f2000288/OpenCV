# Assignment :-3
import cv2


camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')
recorder = cv2.VideoWriter("my_video1.avi", codec, 20, (frame_width,frame_height))

user_input = int(input("Do you want to start Camera If yes Press 1 otherwise 0\n"))

frames = []
if user_input == 1:
    while True:
        success, image = camera.read()

        if not success:
            print("Could't read the frame")
            break
        cv2.imshow("Recording live", image)
        frames.append(image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Ask whether to save
    ask_to_save = int(input("Do you want to save recording? Press 1 for Yes, 0 for No:\n"))

    if ask_to_save == 1:
        print("Saving video...")
        for f in frames:
            recorder.write(f)
        print("Video saved as my_video1.avi")
    else:
        print("Recording discarded.")
    camera.release()
    recorder.release()
    cv2.destroyAllWindows()
else:
    print("Not selected any option to start camera")