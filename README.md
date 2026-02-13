# Traffic Sign Detection using YOLO & Streamlit

## Overview

This project is a Traffic Sign Detection web application built using
Ultralytics YOLO and Streamlit. It supports real-time webcam detection,
image uploads, and video uploads.

## Project Structure

    Traffic-Sign-Detection/
    │
    ├── app.py
    ├── best.pt
    ├── req.txt
    │
    ├── Images/                 # Sample test images
    ├── Results images/         # Predicted output images
    │
    ├── Model - Notebook/
    │   └── traffic-object-detection-yolov26n.ipynb
    │
    └── README.md

## Dataset Categories

Traffic signs in this dataset are grouped into four main categories:

### Prohibitory

-   speed limit
-   no overtaking
-   no traffic both ways
-   no trucks

### Danger

-   priority at next intersection
-   danger
-   bend left
-   bend right
-   bend
-   uneven road
-   slippery road
-   road narrows
-   construction
-   traffic signal
-   pedestrian crossing
-   school crossing
-   cycles crossing
-   snow
-   animals

### Mandatory

-   go right
-   go left
-   go straight
-   go right or straight
-   go left or straight
-   keep right
-   keep left
-   roundabout

### Other

-   restriction ends
-   priority road
-   give way
-   stop
-   no entry

## Model Training

The model was trained using Ultralytics YOLO. The training notebook is
located in:

Model - Notebook/traffic-object-detection-yolov26n.ipynb

The trained weights file `best.pt` is used for inference inside
`app.py`.

## Installation

1.  Clone the repository: git clone
    https://github.com/Moaz-Abdelazim/traffic-sign-detection.git cd
    traffic-sign-detection

2.  (Optional) Create virtual environment: python -m venv venv

3.  Install dependencies: pip install -r req.txt

## Run the Application

    streamlit run app.py

## Features

-   Live webcam detection
-   Image upload detection (.jpg, .png)
-   Video upload detection (.mp4, .avi)
-   Bounding boxes and class labels visualization

## Testing

-   Use images from the `Images/` folder
-   View predicted outputs inside `Results images/`

## Technologies Used

-   Python
-   Ultralytics YOLO
-   Streamlit
-   OpenCV
-   NumPy
-   Pillow

## Author

Moaz Mohammed AbdElazim\
GitHub: https://github.com/Moaz-Abdelazim
