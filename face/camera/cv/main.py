import cv2
import dlib

def face_detect_cv(image):
    cascade_path = "/usr/local/opt/opencv3/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_path)
    facerect = cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
    
    color = (255, 255, 255)

    if len(facerect) > 0:
        for rect in facerect:
            cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)
    cv2.imshow("image",image)
    

if __name__ == "__main__":
	cap = cv2.VideoCapture(0)

	cascade_path = "/usr/local/opt/opencv3/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
	cascade = cv2.CascadeClassifier(cascade_path)
	print(cascade)

	while(True):
	    # Capture frame-by-frame
	    ret, frame = cap.read()

	    face_detect_cv(frame)

	    # Display the resulting frame
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break

	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()












