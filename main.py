import dlib
import cv2

# Task 1
im = cv2.imread('variant-1.jpg')
gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray_im)
cv2.waitKey(0)

print(gray_im)
print('Type:', type(gray_im))
print('Shape:', gray_im.shape)
cv2.imwrite('gray_variant-1.jpg', gray_im)

print('Done.')

# Task 2

model_detector = dlib.simple_object_detector("tld.swm")
font = cv2.FONT_HERSHEY_COMPLEX
cap = cv2.VideoCapture(0)
img = cv2.imread('fly64.png')
img = cv2.resize(img, (20, 20))
img_height, img_width, _ = img.shape

while True:
    ret, frame = cap.read()

    all = model_detector(frame)
    for square in all:
        x = square.left()
        y = square.top()
        w = square.right()
        h = square.bottom()
        cv2.rectangle(frame, (x, y), (w + x, h + y), (255, 0, 0), 1)
        center = ((int((x + w) / 2)), (int((y + h) / 2)))
        x_center = center[0]
        y_center = center[1]
        string = str(x_center) + " " + str(y_center)
        cv2.circle(frame, center, 5, (255, 0, 0), 2)
        if x_center < 450 and y_center < 300:
            cv2.putText(frame, string, center, font, 0.5, (200, 0, 0))

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
