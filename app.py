from flask import Flask, render_template
from flask_socketio import SocketIO
import cv2
import mediapipe as mp
import numpy as np
import threading
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'teleprompter-secret-key'
socketio = SocketIO(app, cors_allowed_origins="*")

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hand_tracker = None
tracking_thread = None
tracking_active = False
last_hand_y = None


class HandTracker:
    def __init__(self):
        self.hands = mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.cap = None

    def start_camera(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            return False
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        return True

    def stop_camera(self):
        if self.cap:
            self.cap.release()
            self.cap = None

    def is_hand_open(self, landmarks):
        thumb_tip = landmarks[4]
        thumb_ip = landmarks[3]
        index_tip = landmarks[8]
        index_pip = landmarks[6]
        middle_tip = landmarks[12]
        middle_pip = landmarks[10]
        ring_tip = landmarks[16]
        ring_pip = landmarks[14]
        pinky_tip = landmarks[20]
        pinky_pip = landmarks[18]

        fingers_open = 0
        
        if thumb_tip.y < thumb_ip.y:
            fingers_open += 1
        
        if index_tip.y < index_pip.y:
            fingers_open += 1
        
        if middle_tip.y < middle_pip.y:
            fingers_open += 1
        
        if ring_tip.y < ring_pip.y:
            fingers_open += 1
        
        if pinky_tip.y < pinky_pip.y:
            fingers_open += 1

        return fingers_open >= 3

    def process_frame(self):
        if not self.cap:
            return None

        success, frame = self.cap.read()
        if not success:
            return None

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        results = self.hands.process(rgb_frame)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing = mp_drawing
                self.draw_landmarks(frame, hand_landmarks)
                
                index_tip = hand_landmarks.landmark[8]
                hand_y = index_tip.y
                
                return {
                    'detected': True,
                    'hand_open': self.is_hand_open(hand_landmarks.landmark),
                    'y_position': hand_y,
                    'speed': 0
                }
        
        return {'detected': False}

    def draw_landmarks(self, frame, hand_landmarks):
        mp_drawing.draw_landmarks(
            frame,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=4),
            mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2)
        )


def tracking_loop():
    global tracking_active, last_hand_y
    
    tracker = HandTracker()
    
    if not tracker.start_camera():
        socketio.emit('camera_error', {'message': 'Impossible d\'accéder à la caméra'})
        return
    
    last_y = None
    
    while tracking_active:
        result = tracker.process_frame()
        
        if result:
            if result['detected']:
                if last_y is not None:
                    result['speed'] = (last_y - result['y_position']) * 500
                
                last_y = result['y_position']
                socketio.emit('hand_detected', result)
            else:
                last_y = None
                socketio.emit('hand_not_detected')
        
        socketio.sleep(int(0.03))
    
    tracker.stop_camera()


@socketio.on('connect')
def handle_connect():
    print('Client connecté')


@socketio.on('disconnect')
def handle_disconnect():
    global tracking_active
    tracking_active = False


@socketio.on('start_hand_tracking')
def handle_start_tracking():
    global tracking_active, tracking_thread, hand_tracker
    
    if tracking_active:
        return
    
    tracking_active = True
    tracking_thread = threading.Thread(target=tracking_loop)
    tracking_thread.daemon = True
    tracking_thread.start()


@socketio.on('stop_hand_tracking')
def handle_stop_tracking():
    global tracking_active
    tracking_active = False


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    print('=' * 50)
    print('🎬 AI Téléprompteur')
    print('=' * 50)
    print('Ouvrez http://localhost:8080 dans votre navigateur')
    print('=' * 50)
    socketio.run(app, host='0.0.0.0', port=8080, debug=True, allow_unsafe_werkzeug=True)
