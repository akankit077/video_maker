import sys
import os
import cv2
from natsort import natsorted


def create_video(path):
    """
    This function will generate the video by taking the frames one by one in
    expected sequence and print the path to the generated video file
    :param path: path to the directory containing video frames
    :return: path to the generated video file
    """
    video_name = 'myVideo.avi'

    # if video with file name 'myVideo.avi' already exists, then appending
    # number in filename like 'myVideo(1).avi'
    file_number = 1
    while os.path.exists(video_name):
        video_name = f'myVideo({file_number}).avi'
        file_number += 1

    images = [img for img in os.listdir(path)
              if img.endswith(".jpg") or
                 img.endswith(".jpeg") or
                 img.endswith(".png")]
    # Sorting images so that when we append images into video, the images should come in
    # expected order. Natsorted algo is used so that "image_1.jpeg" will come first and
    # not after "image_09"
    images = natsorted(images)

    frame = cv2.imread(os.path.join(path, images[0]))

    # setting the frame width, height width equal to the width, height of first image
    # assuming all images have the same width and height
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 25, (width, height))

    # Appending the images to the video one by one
    for image in images:
        video.write(cv2.imread(os.path.join(path, image)))

    # Deallocating memories taken for window creation
    cv2.destroyAllWindows()
    video.release()

    # printing path to generated video file
    print(f"Path to video file: {os.getcwd()}/{video_name}")


def main(args):
    """
    This function will check if the path to frames is passed or not correctly
    and then call the create_video function if everything is fine
    """
    if len(args) < 2:
        print("Please pass path to the folder having video frames.")
        sys.exit(1)
    elif len(args) > 2:
        print(f"{len(args)-1} arguments passed, 1 needed")
        sys.exit(1)
    create_video(args[1])


if __name__=='__main__':
    main(sys.argv)
