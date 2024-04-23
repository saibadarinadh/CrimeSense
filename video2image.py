import cv2

def extract_frames(video_path, output_path):
    # Open the video file
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0

    # Loop through the video and extract frames
    while success:
        # Write the frame to the output folder
        cv2.imwrite(output_path + "/frame%d.jpg" % count, image)
        success, image = vidcap.read()
        count += 1

    print("Frames extracted successfully.")

# Example usage
video_path = "C:/Users/Badari/OneDrive/Desktop/crime/video/A portal to hell at an aluminum plant that swallowed up the entire shop in a matter of seconds..mp4"
output_path = "C:/Users/Badari/OneDrive/Desktop/crime/images"
extract_frames(video_path, output_path)


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
video_path = "video"
output_path = "images"
extract_frames(video_path, output_path)

# import os
# import cv2

# def extract_frames(video_path, output_path):
#     # Open the video file
#     vidcap = cv2.VideoCapture(video_path)
#     success, image = vidcap.read()
#     count = 0

#     # Get the frame rate of the video
#     fps = int(vidcap.get(cv2.CAP_PROP_FPS))

#     # Loop through the video and extract frames at the specified interval
#     while success:
#         # Write the frame to the output folder
#         cv2.imwrite(output_path + "/frame%d.jpg" % count, image)
        
#         # Move to the next frame at the specified interval (1 frame per second)
#         for _ in range(fps):
#             success, image = vidcap.read()
#             count += 1

#     print("Frames extracted successfully.")

# # Get the current working directory
# current_directory = os.getcwd()

# # Example usage
# video_folder = "video"
# video_file = "fit - Made with Clipchamp.mp4"
# video_path = os.path.join(current_directory, video_folder, video_file)
# output_path = "images"
# extract_frames(video_path, output_path)
