import os
import cv2
import numpy as np
from collections import Counter
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input

# Function to extract frames from a video
def extract_frames(video_path, output_path):
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    while success:
        cv2.imwrite(output_path + "/frame%d.jpg" % count, image)
        for _ in range(fps):
            success, image = vidcap.read()
            count += 1

    print("Frames extracted successfully.")

# Function to preprocess an image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)  # Add a batch dimension
    x = preprocess_input(x)
    return x

# Load the saved model
model = load_model("crime_detection_model_optimized_1.h5")

# Define the directory containing the images
image_dir = "C:/Users/Badari/OneDrive/Desktop/crime/images"

# Define crime classes
crime_classes = ['Abuse', 'Arrest', 'Arson', 'Assault', 'Burglary', 'Explosion', 'Fighting',
                 'Normal Videos', 'Road Accidents', 'Robbery', 'Shooting', 'Shoplifting', 'Stealing', 'Vandalism']

# List to store predictions for each image
predictions_list = []

# Define the directory containing the videos
video_dir = "C:/Users/Badari/OneDrive/Desktop/crime/video"

# Get a list of all files in the video directory
video_files = os.listdir(video_dir)

# Filter for video files (assuming they have extensions like .mp4, .avi, etc.)
video_files = [file for file in video_files if file.lower().endswith((".mp4", ".avi", ".mov"))]

# Check if there are any video files in the directory
if not video_files:
    print("No video files found in the directory.")
else:
    # Select the first video file
    selected_video = os.path.join(video_dir, video_files[0])
    print("Selected video file:", selected_video)

    # Extract frames from the selected video
    extract_frames(selected_video, image_dir)

    # Iterate through each image in the directory
    for filename in os.listdir(image_dir):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            image_path = os.path.join(image_dir, filename)
            # Preprocess the image
            x = preprocess_image(image_path)
            # Make prediction
            predictions = model.predict(x)
            # Get the predicted class index
            predicted_class_index = np.argmax(predictions[0])
            # Map the predicted class index to the corresponding crime class
            predicted_crime_class = crime_classes[predicted_class_index]
            # Store the prediction
            predictions_list.append(predicted_crime_class)

    # Count occurrences of each crime class
    crime_class_counts = Counter(predictions_list)

    # Calculate the total number of predictions
    total_predictions = len(predictions_list)

    # Print predictions for each image
    for crime_class, count in crime_class_counts.items():
        percentage = (count / total_predictions) * 100
        print(f"{crime_class} -- {percentage:.2f}%")
