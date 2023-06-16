import cv2              # for a camera control
import mediapipe as mp  # for a hand detection
import pyautogui        # for a event fire

# for a capture video with your pc camera
cap = cv2.VideoCapture(0)

# detect hand movement
hand_detector = mp.solutions.hands.Hands()

# draw point in your hand
drawing_utils = mp.solutions.drawing_utils
y = 0


while True:
    _, frame = cap.read()
    # for a flip your camera view
    frame = cv2.flip(frame, 1)

    # for a best camera capture view is rgb
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # for detect your hand
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            # for draw a points in hand and show in camera
            drawing_utils.draw_landmarks(rgb_frame, hand)
            landmarks = hand.landmark

            for id, landmark in enumerate(landmarks):
                # for a forefinger location
                if id == 8:
                    x = int(landmark.x * 640)
                    y = int(landmark.y * 480)
                    h = int(landmark.x * 2700)
                    m = int(landmark.y * 1700)
                    print(h, m)
                    # for a draw circle in your forefinger
                    cv2.circle(img=frame, center=(x, y), radius=15, color=(0, 255, 255))
                    pyautogui.moveTo(h, m)

                # for a thumb location
                if id == 4:
                    thumb_x = int(landmark.x * 640)
                    thumb_y = int(landmark.y * 480)
                    thumb_h = int(landmark.x * 2500)
                    thumb_m = int(landmark.y * 1600)

                    # for a draw circle in your thumb
                    cv2.circle(img=frame, center=(thumb_x, thumb_y), radius=15, color=(0, 255, 255))

                    # for a click event
                    if abs(y - thumb_y) < 18:
                        pyautogui.click()
                        pyautogui.sleep(1)
                        print("click")

    # show a output in camera
    cv2.imshow('mouse', frame)
    cv2.waitKey(1)
