# Traffic Sign Detection & Video Analytics Web App

## Overview

This project is a full web-based Traffic Sign Detection application
built using Ultralytics YOLO and Streamlit.

The system supports:

-   Real-time webcam detection
-   Image upload inference
-   Full video processing with downloadable results

The application performs object detection on traffic signs and allows
users to visualize and download processed outputs directly from the web
interface.

------------------------------------------------------------------------

## Key Features

-   Real-time inference using webcam
-   Image upload detection (.jpg, .png, .jpeg)
-   Video upload detection (.mp4, .avi)
-   Batch video processing (frame-by-frame inference)
-   Download processed image results
-   Download processed video results
-   Bounding boxes with class labels and confidence scores
-   Progress tracking during video processing

------------------------------------------------------------------------

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

------------------------------------------------------------------------

## Dataset Categories

Traffic signs in this dataset are grouped into four main categories:

### Prohibitory

-   speed limit\
-   no overtaking\
-   no traffic both ways\
-   no trucks

### Danger

-   priority at next intersection\
-   danger\
-   bend left\
-   bend right\
-   bend\
-   uneven road\
-   slippery road\
-   road narrows\
-   construction\
-   traffic signal\
-   pedestrian crossing\
-   school crossing\
-   cycles crossing\
-   snow\
-   animals

### Mandatory

-   go right\
-   go left\
-   go straight\
-   go right or straight\
-   go left or straight\
-   keep right\
-   keep left\
-   roundabout

### Other

-   restriction ends\
-   priority road\
-   give way\
-   stop\
-   no entry

------------------------------------------------------------------------

## Model Training

The model was trained using Ultralytics YOLO.

Training notebook: Model -
Notebook/traffic-object-detection-yolov26n.ipynb

The trained weights file `best.pt` is used for inference inside
`app.py`.

------------------------------------------------------------------------

## Installation

1.  Clone the repository:

git clone https://github.com/Moaz-Abdelazim/traffic-sign-detection.git\
cd traffic-sign-detection

2.  (Optional) Create virtual environment:

python -m venv venv

3.  Install dependencies:

pip install -r req.txt

------------------------------------------------------------------------

## Run the Application

streamlit run app.py

After running the app, choose one of the following modes from the
sidebar:

-   Live Camera
-   Upload Image
-   Upload Video

------------------------------------------------------------------------

## Technologies Used

-   Python
-   Ultralytics YOLO
-   Streamlit
-   OpenCV
-   NumPy
-   Pillow

------------------------------------------------------------------------

## Author

Moaz Mohammed AbdElazim\
GitHub: https://github.com/Moaz-Abdelazim
