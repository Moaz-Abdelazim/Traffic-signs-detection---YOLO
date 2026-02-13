from ultralytics import YOLO
import streamlit as st
import cv2
from PIL import Image
import tempfile
import numpy as np
import os

# Load model
model = YOLO("best.pt")

st.title("Traffic Sign Detection")
page = st.sidebar.selectbox("Choose Mode", ["Live Camera", "Upload Image/Video"])

# =======================
# LIVE CAMERA PAGE
# =======================
if page == "Live Camera":
    st.header("Live Camera Feed")

    cap = cv2.VideoCapture(0)
    run = st.checkbox("Run Camera")

    frame_placeholder = st.empty()

    while run:
        ret, frame = cap.read()
        if not ret:
            st.write("Camera not detected")
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = model(frame_rgb)[0].plot()
        frame_placeholder.image(output, channels="RGB")

    cap.release()

# =======================
# UPLOAD PAGE
# =======================
elif page == "Upload Image/Video":
    st.header("Upload Image or Video")

    uploaded_file = st.file_uploader(
        "Choose a file",
        type=["jpg", "png", "jpeg", "mp4", "avi"]
    )

    if uploaded_file is not None:

        # ================= IMAGE =================
        if uploaded_file.type.startswith("image"):

            image = Image.open(uploaded_file)
            frame = np.array(image)

            result = model(frame)[0]
            output = result.plot()

            # عرض الصورة
            st.image(output, channels="RGB", caption="Prediction")

            # حفظ الصورة
            output_path = "output_image.jpg"
            cv2.imwrite(output_path, cv2.cvtColor(output, cv2.COLOR_RGB2BGR))

            with open(output_path, "rb") as file:
                st.download_button(
                    label="Download Result Image",
                    data=file,
                    file_name="prediction.jpg",
                    mime="image/jpeg"
                )

        # ================= VIDEO =================
        elif uploaded_file.type.startswith("video"):

            st.write("Processing video... Please wait.")

            temp_input = tempfile.NamedTemporaryFile(delete=False)
            temp_input.write(uploaded_file.read())
            temp_input.close()

            cap = cv2.VideoCapture(temp_input.name)

            # خد خصائص الفيديو الأصلية
            fps = cap.get(cv2.CAP_PROP_FPS)
            if fps <= 0:
                fps = 25

            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

            output_path = "output_video.mp4"

            # استخدم H264 بدل mp4v (أهم نقطة)
            fourcc = cv2.VideoWriter_fourcc(*'avc1')
            out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            progress = st.progress(0)
            frame_count = 0

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                results = model(frame)[0]
                plotted = results.plot()

                out.write(plotted)

                frame_count += 1
                if total_frames > 0:
                    progress.progress(frame_count / total_frames)

            cap.release()
            out.release()

            st.success("Video processing completed!")

            # اقرأ الفيديو بعد ما يتقفل
            with open(output_path, "rb") as f:
                video_bytes = f.read()

            st.video(video_bytes)

            st.download_button(
                "Download Result Video",
                data=video_bytes,
                file_name="prediction.mp4",
                mime="video/mp4"
            )