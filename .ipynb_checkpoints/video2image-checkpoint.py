# import cv2

# def extract_frames(video_path, output_path):
#     # Open the video file
#     vidcap = cv2.VideoCapture(video_path)
#     success, image = vidcap.read()
#     count = 0

#     # Loop through the video and extract frames
#     while success:
#         # Write the frame to the output folder
#         cv2.imwrite(output_path + "/frame%d.jpg" % count, image)
#         success, image = vidcap.read()
#         count += 1

#     print("Frames extracted successfully.")

# # Example usage
# video_path = "C:/Users/Badari/Downloads/countdown_-_2637 (360p).mp4"
# output_path = "C:/Users/Badari/OneDrive/Desktop/test-1"
# extract_frames(video_path, output_path)


import cv2

def extract_frames(video_path, output_path):
    # Open the video file
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0

    # Get the frame rate of the video
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))

    # Loop through the video and extract frames at the specified interval
    while success:
        # Write the frame to the output folder
        cv2.imwrite(output_path + "/frame%d.jpg" % count, image)
        
        # Move to the next frame at the specified interval (1 frame per second)
        for _ in range(fps):
            success, image = vidcap.read()
            count += 1

    print("Frames extracted successfully.")

# Example usage
video_path = "input_video.mp4"
output_path = "output_frames"
extract_frames(video_path, output_path)
