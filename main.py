import cv2
import mediapipe as mp
import pydirectinput as pdi

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
tip_ids = [4, 8, 12, 16, 20]

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 340)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 280)

current_key = None

blur_value = 7
transparency = 0.4

landmark_drawing_spec = mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=1)
connection_drawing_spec = mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    panel_width = 120 
    panel_height = 60 
    panel_y = 20
    brake_x = 20
    gas_x = frame.shape[1] - panel_width - 20
    spacing = 20
    
    overlay = frame.copy()
    cv2.rectangle(overlay, (brake_x, panel_y), (brake_x + panel_width, panel_y + panel_height), (50, 50, 50), -1)
    cv2.rectangle(overlay, (gas_x, panel_y), (gas_x + panel_width, panel_y + panel_height), (50, 50, 50), -1)
    
    overlay = cv2.GaussianBlur(overlay, (blur_value, blur_value), 0)
    cv2.addWeighted(overlay, transparency, frame, 1 - transparency, 0, frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                landmark_drawing_spec=landmark_drawing_spec,
                connection_drawing_spec=connection_drawing_spec)
            
            landmarks = []
            for lm in hand_landmarks.landmark:
                h, w, _ = frame.shape
                landmarks.append((int(lm.x * w), int(lm.y * h)))
            
            fingers = []
            hand_type = results.multi_handedness[0].classification[0].label
            
            if (hand_type == "Right" and landmarks[tip_ids[0]][0] > landmarks[tip_ids[0]-1][0]) or \
               (hand_type == "Left" and landmarks[tip_ids[0]][0] < landmarks[tip_ids[0]-1][0]):
                fingers.append(1)
            else:
                fingers.append(0)
            
            for id in range(1, 5):
                if landmarks[tip_ids[id]][1] < landmarks[tip_ids[id]-2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            
            total_fingers = sum(fingers)
            
            new_key = None
            if total_fingers <= 1:  
                brake_overlay = frame.copy()
                cv2.rectangle(brake_overlay, (brake_x, panel_y), (brake_x + panel_width, panel_y + panel_height), (30, 30, 150), -1)
                brake_overlay = cv2.GaussianBlur(brake_overlay, (blur_value, blur_value), 0)
                cv2.addWeighted(brake_overlay, transparency, frame, 1 - transparency, 0, frame)
                
                cv2.putText(frame, "BRAKE", (brake_x + 10, panel_y + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (180, 180, 255), 2)
                new_key = 'left'
            
            elif total_fingers >= 4: 
                gas_overlay = frame.copy()
                cv2.rectangle(gas_overlay, (gas_x, panel_y), (gas_x + panel_width, panel_y + panel_height), (30, 150, 30), -1)
                gas_overlay = cv2.GaussianBlur(gas_overlay, (blur_value, blur_value), 0)
                cv2.addWeighted(gas_overlay, transparency, frame, 1 - transparency, 0, frame)
                
                cv2.putText(frame, "GAS", (gas_x + 30, panel_y + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (180, 255, 180), 2)
                new_key = 'right'
            
            if new_key != current_key:
                if current_key:
                    pdi.keyUp(current_key)
                if new_key:
                    pdi.keyDown(new_key)
                current_key = new_key
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    cv2.putText(frame, f"FPS: {int(fps)}", (10, frame.shape[0]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
    cv2.imshow("Hand Controller", frame)
    if cv2.waitKey(1) == ord('q'):
        break

if current_key:
    pdi.keyUp(current_key)
cap.release()
cv2.destroyAllWindows()