# API Documentation

## Index
- [**Home**](#home)

## Introduction
Welcome to the API documentation for CameraAI, a face recognition application.

This documentation provides an overview of the endpoints available in the CameraAI API. It includes details about each endpoint, the expected request and response formats, and additional information to help you effectively use the API.

## Getting Started
To get started with CameraAI, follow these steps:

1. Clone the repository to your local machine.
2. Install the required Python packages using the following command:
```bash
pip install -r requirements.txt"
```
3. Run the application using the command: 
```bash
python run.py
```
4. Access the application in your web browser at http://localhost:1102.

## Endpoints
- [Recognize Face](#recognize-face)
- [Get Detection Log](#get-detection-log)
- [Toggle Capture](#toggle-capture)
- [Toggle Video](#toggle-video)
- [Save Backlog to File](#save-backlog-to-file)
- [Get Emotion Statistics](#get-emotion-statistics)

---

## Home

**URL:** /
**Method:** GET

Renders the home page of the application.

---

## Recognize Face

**URL:** /recognize_face
**Method:** GET

Streams frames for recognizing faces from the camera.

**Response:**
- The response is a streaming of frames in JPEG format.

---

## Get Detection Log

**URL:** /get_detection_log
**Method:** GET

Returns the detection log containing information about detected faces.

**Response:**
- The response is a JSON array containing detection log messages.

---

## Toggle Capture

**URL:** /toggle_capture
**Method:** POST

Toggles the capture mode for capturing images.

---

## Toggle Video

**URL:** /toggle_video
**Method:** POST

Toggles the video mode for capturing video.

---

## Save Backlog to File

**URL:** /save_backlog_to_file
**Method:** GET

Saves the detection backlog to a file.

---

## Get Emotion Statistics

**URL:** /get_emotion_statistics
**Method:** GET

Returns the statistics of detected emotions.

---

## Output Files

The CameraAI project generates the following output files:

- Captured Images: The images captured during the face recognition process are saved in the `/output/captured_images` folder. The filenames follow the format `captured_YYYYMMDDHHMMSS.jpg`.

- Captured Video: If the video mode is enabled, the captured frames are saved as a video in the `/output/captured_video.mp4` file.

---

## Configuration Class

### location_text(self, top, right, bottom, left)

**Description:** Returns a formatted string describing the location of a detected face.

**Parameters:**
- `top` (int): The top coordinate of the bounding box.
- `right` (int): The right coordinate of the bounding box.
- `bottom` (int): The bottom coordinate of the bounding box.
- `left` (int): The left coordinate of the bounding box.

**Returns:** 
- `location_text` (str): The formatted location text.

---

## BacklogSaver Class

### add_to_backlog(self, log_message)

**Description:** Adds a log message to the backlog with a timestamp.

**Parameters:**
- `log_message` (str): The log message to be added.

**Returns:** 
- None

### save_to_file(self, filename)

**Description:** Saves the backlog to a file.

**Parameters:**
- `filename` (str): The name of the file to save the backlog to.

**Returns:** 
- None

### clear_backlog(self)

**Description:** Clears the backlog.

**Parameters:** 
- None

**Returns:** 
- None

## Dependencies

This project depends on the following Python packages:

- click==8.1.3
- deepface==0.0.79
- dlib==19.24.0
- face_recognition_models==1.2.2
- Flask==2.2.2
- Flask_DebugToolbar==0.13.1
- Flask_SocketIO==5.3.5
- numpy==1.24.1
- opencv_contrib_python==4.7.0.68
- opencv_python==4.7.0.68
- Pillow==10.0.0
- scikit_learn==1.2.2
- setuptools==58.1.0
- waitress==2.1.2

Make sure to install these dependencies to use the CameraAI project.

---

*This is a comprehensive example for illustration purposes.*
