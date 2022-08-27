import cv2
import mediapipe as mp
import pyautogui
import pyautogui as pa

cam = cv2.VideoCapture(0)
face = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
while True:
    _, frame = cam.read()
    frmae = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face.process(rgb_frame)
    landmarks = output.multi_face_landmarks
    frmae_h, frame_w, _ = frame.shape
    if landmarks:
        landmark = landmarks[0].landmark
        for id, landm in enumerate(landmark[474:478]):
            x = int(landm.x * frame_w)
            y = int(landm.y * frmae_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_X = 2 * screen_w / frame_w * x
                screen_Y = 2 * screen_h / frmae_h * y
                pyautogui.moveTo(screen_X, screen_Y)
    cv2.imshow('Eye control mouse', frame)
    cv2.waitKey(1)
