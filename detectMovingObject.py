# -*- coding: utf-8 -*-
import cv2
import numpy as np

# caculate the diff of frame
def frame_sub(img1, img2, img3, th):
    diff1 = cv2.absdiff(img1, img2)
    diff2 = cv2.absdiff(img2, img3)

    diff = cv2.bitwise_and(diff1, diff2)

    diff[diff < th] = 0
    diff[diff >= th] = 255
    
    mask = cv2.medianBlur(diff, 5)

    return diff


def main():
    min_moment = 1000

    cap = cv2.VideoCapture(0)
    
    frame1 = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
    frame2 = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
    frame3 = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
    
    cnt = 0

    while(cap.isOpened()):
        mask = frame_sub(frame1, frame2, frame3, th=10)

        moment = cv2.countNonZero(mask)

        if moment > min_moment:
            print("object is detectÅF", cnt)
            filename = "frame" + str(cnt) + ".jpg"
            cv2.imwrite(filename, frame2)
            cnt += 1

        cv2.imshow("Frame2", frame2)
        cv2.imshow("Mask", mask)

        frame1 = frame2
        frame2 = frame3
        frame3 = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()