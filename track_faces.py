import os
import cv2
import csv
import time
from datetime import datetime
import face_recognition

def mark_attendance(name):
    date = datetime.now()
    with open('data/attendance.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([date, name])

def track_faces():
    cap = cv2.VideoCapture(0)

    with open('data/student_details.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        student_details = {row['Name']: row['ID'] for row in reader}

    known_face_encodings = []
    known_names = []
    for file_name in os.listdir('data'):
        if file_name.endswith('.jpg'):
            img = face_recognition.load_image_file(f'data/{file_name}')
            face_encoding = face_recognition.face_encodings(img)[0]
            known_face_encodings.append(face_encoding)
            known_names.append(file_name.split('.')[0])

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                match_index = matches.index(True)
                name = known_names[match_index]

                top, right, bottom, left = face_location
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.putText(frame, name, (left + 6, top - 15,), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

                if cv2.waitKey(1) & 0xFF == ord('c'):
                    mark_attendance(name)
                    cap.release()
                    cv2.destroyAllWindows()
                    
        new_height = 450
        new_width = 800
        frame = cv2.resize(frame, (new_width, new_height))
        bkg=cv2.imread("background.jpg")
        bkg[180:180 + new_height, 240:240 + new_width] = frame
        cv2.imshow('FACE RECOGNITION ATTENDANCE SYSTEM', bkg)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    track_faces()