import cv2
import os
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
	help="path to images to merge into video")
ap.add_argument("-v", "--video_name", required=True,
	help="name of resulting video")
args = vars(ap.parse_args())

video_name = args["video_name"] + ".avi"
images_path = args["images"]

images = [img for img in os.listdir(images_path) if img.endswith(".png")]
if len(images) == 0:
	print("No images found for path: %s" %  images_path)
else:
	print("Processing %d images now." % len(images_path))
	frame = cv2.imread(os.path.join(images_path, images[0]))
	height, width, layers = frame.shape

	video = cv2.VideoWriter(video_name, 0, 9, (width,height))
	fontFace = cv2.FONT_HERSHEY_SIMPLEX
	fontScale = 2
	thickness = 3

	for i,image in enumerate(sorted(images)):
		print("Frame %d" % i)
		img = cv2.imread(os.path.join(images_path, image))
		text = "Frame "+ str(i)
		cv2.putText(img, text, (10,50), fontFace, 2, (255,255,255), thickness, cv2.LINE_AA)
		video.write(img)

	cv2.destroyAllWindows()
	video.release()
	print("Video %s successfully created" % video_name)