import cv2
import os
import time


def run(vidPath, frames=300):
    start_time = time.time()
    # read video file
    id = vidPath.split("/")[-2]
    photo_path = "/".join(vidPath.split("/")[0:-2])
    create_images(vidPath, photo_path, id, frames)
    stop_time = time.time()
    print(f"all convert time is {(stop_time - start_time):.2f}")

def create_images(vidPath, photo_path, id, frames):
    vidPath = ".".join([vidPath.split(".")[0], "MP4"]) if not os.path.exists(vidPath) else vidPath
    vidcap = cv2.VideoCapture(vidPath)
    # judge whether it opens properly
    if vidcap.isOpened():
        totalFrames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        jump = int(totalFrames / frames)
        count = 1
        frame = jump
        # video frame count interval frequency
        while frame < totalFrames:
            vidcap.set(cv2.CAP_PROP_POS_FRAMES, frame)
            success, image = vidcap.read()
            # store as an image
            cv2.imwrite("{}/{}_image".format(photo_path, id) + str(count) + ".jpg", image)
            count = count + 1
            frame += jump
            cv2.waitKey(1)
        vidcap.release()
    else:
        print("Video unable to process")

vipPath = 'dataset/with_mask/nick/nick.mp4'
run(vipPath)