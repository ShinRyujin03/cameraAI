from flask import Response, render_template, jsonify
from . import app, socketio  # Import socketio từ app
from .Funtion.camera import Camera
from .Funtion.backlog_saver import backlog_saver

camera = Camera(socketio)
@app.route('/')
def index():
    return render_template('A.html')

@app.route('/recognize_face', methods=['GET'])
def recognize_face():
    return Response(camera.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_detection_log', methods=['GET'])
def get_detection_log():
    log_messages = camera.get_detection_log()
    return jsonify(log_messages)

@app.route('/toggle_capture', methods=['POST'])
def toggle_capture():
    enabled = camera.toggle_capture()
    return jsonify({'capture_enabled': enabled})

@app.route('/toggle_video', methods=['POST'])
def toggle_video():
    enabled = camera.toggle_video()
    return jsonify({'video_enabled': enabled})

@app.route('/save_backlog_to_file', methods=['GET'])
def save_backlog_to_file():
    try:
        backlog_saver.save_to_file('/Users/macbookairm1/Desktop/Viettel/CameraAI/output/backlog.txt')
        return jsonify(success=True)
    except Exception as e:
        print("Error saving backlog:", e)
        return jsonify(success=False)


