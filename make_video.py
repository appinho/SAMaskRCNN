import cv2
import os

image_folder = "./results/"
video_name = 'video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 9, (width,height))
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 2
thickness = 3

for i,image in enumerate(sorted(images)):
    img = cv2.imread(os.path.join(image_folder, image))
    text = "Frame "+ str(i)
    cv2.putText(img, text, (10,50), fontFace, 2, (255,255,255), thickness, cv2.LINE_AA)
    video.write(img)

cv2.destroyAllWindows()
video.release()
