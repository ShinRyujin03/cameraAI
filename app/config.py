import os
import time
class Config:
    #key
    key = os.urandom(24)

    #path and file name
    image_filename = 'captured_%Y%m%d%H%M%S.jpg'
    img_folder = '/Users/macbookairm1/Desktop/Viettel/CameraAI/output/captured_images'
    vid_filename = '/Users/macbookairm1/Desktop/Viettel/CameraAI/output/captured_video.mp4'
    backlog_filename = '/Users/macbookairm1/Desktop/Viettel/CameraAI/output/backlog.txt'
    template_path = 'A.html'

    #camera config
     #color and text
    box_color = (222, 154, 68)
    text_color =(222,80,96)
    output_vid_fps = 5.0
    emotion_text = f"Emotion: "
    emotion_text_none = "Emotion: Unknown"
    def location_text(self,top, right, bottom,left):
        return f"Location: top={top}, right={right}, bottom={bottom}, left={left}"