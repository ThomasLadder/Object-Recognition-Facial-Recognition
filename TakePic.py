import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")


while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 113:
        # ESC pressed
        print("q hit, closing camera...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = input('Enter your name : ')
        cv2.imwrite('/Users/thomasyoung/myImages/' + str(img_name) + '.jpg', frame)
        print(str(img_name) + " was entered into the database.")

cam.release()

cv2.destroyAllWindows()
