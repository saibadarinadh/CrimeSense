# CrimeSense - Crime Detection and Analysis

CrimeSense is a machine learning-based crime detection system designed to classify and analyze crime-related activities from video footage. The project uses deep learning techniques with the MobileNetV2 architecture to train a model for this purpose.

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Project Structure](#project-structure)
4. [Setup and Installation](#setup-and-installation)
5. [Model Training](#model-training)
6. [Video Processing and Crime Detection](#video-processing-and-crime-detection)
7. [Usage Example](#usage-example)
8. [Credits and Acknowledgments](#credits-and-acknowledgments)
9. [License](#license)

## Introduction
CrimeSense provides a framework for training a crime detection model using MobileNetV2 and then utilizing the trained model to classify activities from video footage. The project includes scripts for training, data augmentation, and video processing to extract frames and classify them.

## Prerequisites
Before running this code, ensure you have the following installed on your system:
- Python 3.7 or higher
- TensorFlow 2.0 or higher
- OpenCV
- Required Python libraries: `numpy`, `os`, `glob`, `collections`, `tensorflow.keras.preprocessing`, etc.

## Project Structure
- `training_code.py`: Script for training the crime classification model.
- `video_processing.py`: Script for extracting frames from videos and classifying them.
- `requirements.txt`: File listing all required Python libraries for easy installation.

## Setup and Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/saibadarinadh/CrimeSense.git
