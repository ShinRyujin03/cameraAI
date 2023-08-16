import cv2
import face_recognition
import time
import os
from deepface import DeepFace
from app.funtion.backlog_saver import backlog_saver
from app.config import Config
class Camera:
    def __init__(self, socketio):
        self.cap = cv2.VideoCapture(1, cv2.CAP_AVFOUNDATION)
        self.socketio = socketio
        self.total_image_count = 0  # Tổng số lượng ảnh đã chụp
        self.image_folder = Config.img_folder  # Tên thư mục lưu ảnh
        self.capture_enabled = False  # Trạng thái chụp ảnh
        self.video_enabled = False  # Trạng thái quay video
        self.video_filename = Config.vid_filename  # Tên tệp video
        self.video_writer = None
        self.face_locations = []
        self.last_capture_time = 0
        self.face_emotions = []
        # Tạo thư mục nếu chưa tồn tại
        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder)

    def generate_frames(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            rgb_frame = frame[:, :, ::-1]
            self.face_locations = face_recognition.face_locations(rgb_frame)

            if self.face_locations:
                for i, face_location in enumerate(self.face_locations):
                    top, right, bottom, left = face_location
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    face_image = rgb_frame[top:bottom, left:right]
                    face_emotion = self.detect_emotion(face_image)
                    self.face_emotions.append(face_emotion)  # Thêm cảm xúc vào danh sách

                    if face_emotion is not None:
                        emotion_text = f"Emotion: {face_emotion}"
                        location_text = f"Location: top={top}, right={right}, bottom={bottom}, left={left}"
                        cv2.putText(frame, emotion_text, (left, bottom + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (0, 255, 0), 2)
                        cv2.putText(frame, location_text, (left, bottom + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (0, 255, 0), 2)
                    else:
                        cv2.putText(frame, location_text, (left, bottom + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (0, 255, 0), 2)

                self.capture_image(frame)

                ret, jpeg = cv2.imencode('.jpg', frame)
                frame_bytes = jpeg.tobytes()

                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    def detect_emotion(self, face_image):
        # Sử dụng face_recognition để kiểm tra xem có khuôn mặt trong ảnh hay không
        face_locations = face_recognition.face_locations(face_image)
        if not face_locations:
            return None  # Không có khuôn mặt, không cần phân tích cảm xúc

        # Phân tích cảm xúc bằng DeepFace
        emotions = DeepFace.analyze(face_image, actions=['emotion'],enforce_detection=False)
        emotions_data = emotions
        dominant_emotion = emotions_data[0]['dominant_emotion']
        return dominant_emotion

    def get_emotion_statistics(self):
        emotion_counts = {
            'angry': 0,
            'disgust': 0,
            'fear': 0,
            'happy': 0,
            'sad': 0,
            'surprise': 0,
            'neutral': 0
        }

        for face_emotion in self.face_emotions:
            if face_emotion is not None:
                emotion_counts[face_emotion] += 1

        return emotion_counts

    def write_video_frame(self, frame):
        if self.video_writer is None:
            fourcc = cv2.VideoWriter_fourcc(*'H264')
            self.video_writer = cv2.VideoWriter(self.video_filename, fourcc, 5.0, (frame.shape[1], frame.shape[0]))

        self.video_writer.write(frame)

    def capture_image(self, frame):
        if self.capture_enabled:
            current_time = time.time()
            if current_time - self.last_capture_time >= 1:  # Chờ ít nhất 1 giây giữa mỗi lần chụp
                self.last_capture_time = current_time

                image_filename = os.path.join(self.image_folder, f'captured_{time.strftime("%Y%m%d%H%M%S")}.jpg')
                cv2.imwrite(image_filename, frame)
                print(f"Image captured: {image_filename}")

                self.last_image_filename = image_filename
                self.socketio.emit('image_captured', {
                    'message': f"Image captured at {time.strftime('%Y-%m-%d %H:%M:%S')} as {self.last_image_filename}"},
                                   namespace='/test')
                self.total_image_count += 1
                # Ghi frame vào video
        if self.video_enabled:
            self.write_video_frame(frame)
    def toggle_capture(self):
        self.capture_enabled = not self.capture_enabled
        return self.capture_enabled

    def toggle_video(self):
        if self.video_enabled:
            if self.video_writer is not None:
                self.video_writer.release()  # Ngừng ghi video nếu video_enabled là True và video_writer tồn tại
                self.video_writer = None
            self.video_enabled = False
        else:
            self.video_enabled = True
        return self.video_enabled

    def get_detection_log(self):
        log_messages = []

        for i, location in enumerate(self.face_locations):
            emotion = self.face_emotions[i-1]
            emotion_text = f"Emotion: {emotion}" if emotion is not None else "Emotion: Unknown"
            location_text = f"Face detected at: {location}, {emotion_text}"
            log_messages.append(location_text)

        if self.total_image_count > 0:
            log_messages.append(f"Total images captured: {self.total_image_count}")

        # Thêm thông báo trạng thái chụp ảnh và video
        log_messages.append(f"Capture enabled: {self.capture_enabled}")
        log_messages.append(f"Video enabled: {self.video_enabled}")

        # Thêm thông tin về cảm xúc
        emotion_statistics = self.get_emotion_statistics()
        for face_emotion, count in emotion_statistics.items():
            log_messages.append(f"{face_emotion.capitalize()} count: {count}")

        # Thêm log messages vào backlog_saver
        for message in log_messages:
            backlog_saver.add_to_backlog(message)

        return log_messages


