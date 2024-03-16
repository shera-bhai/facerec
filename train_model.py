import cv2
import csv
import os
import face_recognition
import numpy as np

def capture_face_data():
    cap = cv2.VideoCapture(0)

    face_data = []
    student_details = []
    global student_name

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        face_locations = face_recognition.face_locations(frame)

        if face_locations:
            top, right, bottom, left = face_locations[0]
            face_data.append(frame[top:bottom, left:right])

            student_name = input("Enter Student Name: ")
            student_id = input("Enter Student ID: ")

            student_details.append((student_id, student_name))
            cap.release()
            cv2.destroyAllWindows()

        new_height = 450
        new_width = 800
        frame = cv2.resize(frame, (new_width, new_height))
        bkg=cv2.imread("background.jpg")
        bkg[180:180 + new_height, 240:240 + new_width] = frame
        cv2.imshow('FACE RECOGNITION ATTENDANCE SYSTEM', bkg)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return face_data, student_details

def train_model():
    print('Starting Model...')
    face_data, student_details = capture_face_data()
    print('Data Captured!')

    for i, face_img in enumerate(face_data):
        cv2.imwrite(f'data/{student_name}.jpg', face_img)

    with open('data/student_details.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Name'])
        writer.writerows(student_details)

if __name__ == '__main__':
    train_model()