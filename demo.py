# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""
Created on 2021/5/24 13:46
@Author: Wang Cong
@Email : iwangcong@outlook.com
@Version : 0.1
@File : demo_trt.py
"""
import yolo_deepsort
import cv2
import time

if __name__ == '__main__':

    yolo_engine = './yolov5/yolov5s.engine'
    sort_engine = './deepsort/deepsort.engine'
    capture = cv2.VideoCapture(0)
    yolo_deepsort_test = yolo_deepsort.Yolov5DeepSort(yolo_engine, sort_engine)

    fps = 0.0
    while True:
        ret, img = capture.read()
        if img is None:
            print('No image input!')
            break

        t1 = time.time()
        frame = yolo_deepsort_test.detect_track_frame(img)
        t2 = time.time() - t1
        print(t2*1000)
        cv2.imshow('frame', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

