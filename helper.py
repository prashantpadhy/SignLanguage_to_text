import cv2
import mediapipe as mp

mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils

finger_tips=[8,12,16,20]
thumb_tip=4
class DetectSignLang(object):
    def __init__(self):
        self.cap=cv2.VideoCapture(0)
        self.turnOff=False
    def __del__(self):
        self.cap.release()
    def close(self):
        self.cap.release()
    def get_frame(self):
        success,img=self.cap.read()
        img=cv2.flip(img,1)
        h, w, c = img.shape
        results=hands.process(img)

        if results.multi_hand_landmarks:
            for handlandmark in results.multi_hand_landmarks:
                lm_list=[]
                for id,lm in enumerate(handlandmark.landmark):
                    lm_list.append(lm)
                finger_fold_status = []
                for tip in finger_tips:
                    x,y=int(lm_list[tip].x*w),int(lm_list[tip].y*h)
                    cv2.circle(img,(x,y),15,(255,0,0),cv2.FILLED)

                    if lm_list[tip].x>lm_list[tip-3].x:
                        cv2.circle(img, (x, y), 15, (255, 0, 0), cv2.FILLED)
                        finger_fold_status.append(True)
                    else:
                        finger_fold_status.append(False)
                print(finger_fold_status)

                if all(finger_fold_status):
                    if lm_list[thumb_tip].y < lm_list[thumb_tip-1].y < lm_list[thumb_tip-2].y:
                        print("LIKE")
                        cv2.putText(img,"LIKE",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0, 255),3)
                    if lm_list[thumb_tip].y > lm_list[thumb_tip-1].y > lm_list[thumb_tip-2].y:
                        print("DISLIKE")
                        cv2.putText(img, "DISLIKE", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    if lm_list[thumb_tip].y > lm_list[thumb_tip-1].y < lm_list[thumb_tip-2].y:
                        print("FIST")
                        cv2.putText(img, "FIST", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                else:
                    if lm_list[thumb_tip].x < lm_list[thumb_tip-1].x < lm_list[thumb_tip-2].x and lm_list[8].y < lm_list[7].y and lm_list[12].y < lm_list[11].y and lm_list[16].y < lm_list[15].y and lm_list[20].y < lm_list[19].y:
                        print("STOP")
                        cv2.putText(img, "STOP", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    if lm_list[thumb_tip].y < lm_list[thumb_tip-1].y < lm_list[thumb_tip-2].y and lm_list[8].y < lm_list[7].y and lm_list[12].y > lm_list[9].y and lm_list[16].y > lm_list[13].y and lm_list[20].y < lm_list[19].y:
                        print("ROCK")
                        cv2.putText(img, "ROCK", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    if lm_list[8].y > lm_list[5].y and lm_list[12].y > lm_list[9].y and lm_list[16].y > lm_list[13].y and lm_list[20].y > lm_list[17].y and lm_list[thumb_tip].y < lm_list[thumb_tip-1].y < lm_list[thumb_tip-2].y:
                        print("A")
                        cv2.putText(img, "A", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    if lm_list[thumb_tip].x > lm_list[thumb_tip-1].x > lm_list[thumb_tip-2].x and lm_list[8].y < lm_list[7].y and lm_list[12].y < lm_list[11].y and lm_list[16].y < lm_list[15].y and lm_list[20].y < lm_list[19].y:
                        print("B")
                        cv2.putText(img, "B", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    if lm_list[thumb_tip].y > lm_list[thumb_tip-1].y < lm_list[thumb_tip-2].y and lm_list[8].y > lm_list[7].y < lm_list[5].y and lm_list[12].y > lm_list[11].y < lm_list[9].y and lm_list[16].y > lm_list[15].y < lm_list[13].y and lm_list[20].y > lm_list[19].y < lm_list[17].y:
                        print("C")
                        cv2.putText(img, "C", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    if lm_list[thumb_tip].y < lm_list[thumb_tip-1].y < lm_list[thumb_tip-2].y and lm_list[8].y < lm_list[7].y and lm_list[12].y > lm_list[11].y < lm_list[9].y and lm_list[16].y > lm_list[15].y < lm_list[13].y and lm_list[20].y > lm_list[19].y < lm_list[17].y:
                        print("D")
                        cv2.putText(img, "D", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    if lm_list[thumb_tip].x > lm_list[thumb_tip-1].x > lm_list[thumb_tip-2].x and lm_list[8].y > lm_list[7].y < lm_list[5].y and lm_list[12].y > lm_list[11].y < lm_list[9].y and lm_list[16].y > lm_list[15].y < lm_list[13].y and lm_list[20].y > lm_list[18].y < lm_list[16].y:
                        print("E")
                        cv2.putText(img, "E", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    if lm_list[thumb_tip].y < lm_list[thumb_tip-1].y < lm_list[thumb_tip-2].y and lm_list[8].y > lm_list[6].y and lm_list[12].y < lm_list[11].y and lm_list[16].y < lm_list[15].y and lm_list[20].y < lm_list[19].y:
                        print("F")
                        cv2.putText(img, "F", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    if lm_list[thumb_tip].x < lm_list[thumb_tip-1].x < lm_list[thumb_tip-2].x and lm_list[8].x < lm_list[7].x and lm_list[12].x > lm_list[9].x and lm_list[16].x > lm_list[13].x and lm_list[20].x > lm_list[17].x:
                        print("G")
                        cv2.putText(img, "G", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    if lm_list[thumb_tip].y > lm_list[thumb_tip-1].y < lm_list[thumb_tip-2].y and lm_list[8].x < lm_list[7].x and lm_list[12].x < lm_list[11].x and lm_list[16].x > lm_list[13].x and lm_list[20].x > lm_list[17].x:
                        print("H")
                        cv2.putText(img, "H", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    if lm_list[thumb_tip].x > lm_list[thumb_tip-1].x > lm_list[thumb_tip-2].x and lm_list[8].y > lm_list[5].y and lm_list[12].y > lm_list[9].y and lm_list[16].y > lm_list[13].y and lm_list[20].y < lm_list[19].y:
                        print("I")
                        cv2.putText(img, "I", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    if lm_list[thumb_tip].y > lm_list[thumb_tip-1].y > lm_list[thumb_tip-2].y and lm_list[8].y > lm_list[5].y and lm_list[12].y > lm_list[9].y and lm_list[16].y > lm_list[13].y and lm_list[20].y > lm_list[19].y:
                        print("J")
                        cv2.putText(img, "J", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    if lm_list[thumb_tip].y < lm_list[thumb_tip-1].y < lm_list[thumb_tip-2].y and lm_list[8].y < lm_list[7].y and lm_list[12].y < lm_list[11].y and lm_list[16].y > lm_list[13].y and lm_list[20].y > lm_list[17].y:
                        print("K")
                        cv2.putText(img, "K", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    if lm_list[thumb_tip].x < lm_list[thumb_tip-1].x < lm_list[thumb_tip-2].x and lm_list[8].y < lm_list[7].y and lm_list[12].y > lm_list[9].y and lm_list[16].y > lm_list[13].y and lm_list[20].y > lm_list[17].y:
                        print("L")
                        cv2.putText(img, "L", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    if lm_list[thumb_tip].y < lm_list[thumb_tip-1].y < lm_list[thumb_tip-2].y and lm_list[8].y > lm_list[7].y < lm_list[6].y and lm_list[12].y > lm_list[11].y < lm_list[10].y and lm_list[16].y > lm_list[15].y < lm_list[14].y and lm_list[20].y > lm_list[19].y < lm_list[18].y:
                        print("O")
                        cv2.putText(img, "O", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    if lm_list[thumb_tip].x > lm_list[thumb_tip-1].x > lm_list[thumb_tip-2].x and lm_list[8].y < lm_list[7].y and lm_list[12].y < lm_list[11].y and lm_list[16].y > lm_list[13].y and lm_list[20].y > lm_list[17].y:
                        print("U")
                        cv2.putText(img, "U", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    if lm_list[thumb_tip].y < lm_list[thumb_tip-1].y < lm_list[thumb_tip-2].y and lm_list[8].y < lm_list[7].y and lm_list[12].y < lm_list[11].y and lm_list[16].y < lm_list[15].y and lm_list[20].y > lm_list[17].y:
                        print("W")
                        cv2.putText(img, "W", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    if lm_list[thumb_tip].x < lm_list[thumb_tip-1].x < lm_list[thumb_tip-2].x and lm_list[8].y > lm_list[7].y < lm_list[6].y and lm_list[12].y > lm_list[11].y < lm_list[9].y and lm_list[16].y > lm_list[13].y and lm_list[20].y > lm_list[17].y:
                        print("X")
                        cv2.putText(img, "X", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    if lm_list[thumb_tip].y < lm_list[thumb_tip-1].y < lm_list[thumb_tip-2].y and lm_list[8].y > lm_list[5].y and lm_list[12].y > lm_list[9].y and lm_list[16].y > lm_list[13].y and lm_list[20].y < lm_list[19].y:
                        print("Y")
                        cv2.putText(img, "Y", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    if lm_list[thumb_tip].x > lm_list[thumb_tip-1].x > lm_list[thumb_tip-2].x and lm_list[8].y < lm_list[7].y and lm_list[12].y > lm_list[9].y and lm_list[16].y > lm_list[13].y and lm_list[20].y > lm_list[17].y:
                        print("Z")
                        cv2.putText(img, "Z", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                mpDraw.draw_landmarks(img,handlandmark,mpHands.HAND_CONNECTIONS,mpDraw.DrawingSpec((255,0,0),2,2),mpDraw.DrawingSpec((0,255,0),4,2))
        success, jpeg = cv2.imencode('.jpg', img)
        return (jpeg.tobytes())