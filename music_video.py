import face_recognition
import cv2
import csv
from sklearn import svm

encodings = []
names = []

with open("encodings.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        encodings.append(row)

with open("names.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        names.append(row[0])

clf = svm.SVC(gamma='scale', probability=True)
clf.fit(encodings,names)



input_movie = cv2.VideoCapture("./Videos/wannabe.mp4")
height = int(input_movie.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(input_movie.get(cv2.CAP_PROP_FRAME_WIDTH))
length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))


fourcc = cv2.VideoWriter_fourcc(*'MP4V')
output_movie = cv2.VideoWriter('wannabe.mp4', 0x7634706d, 24.0, (width, height))

# Initialize some variables

face_names = []
frame_number = 0
itzy = ["Lia", "Yeji", "Yuna", "Ryujin", "Chaeryeong"]

while True:
    # Grab a single frame of video
    ret, frame = input_movie.read()
    frame_number += 1

    # Quit when the input video file ends
    if not ret:
        break

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb_frame = frame[:, :, ::-1]
    r = frame.shape[1] / float(rgb_frame.shape[1])

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        name = clf.predict([face_encoding])
        face_names.append(*name)

        # If you had more than 2 faces, you could make this logic a lot prettier
        # but I kept it simple for the demo
        # name = None
        # if match[0]:
        #     name = "Lin-Manuel Miranda"
        # elif match[1]:
        #     name = "Alex Lacamoire"

    # Label the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        if not name:
            continue
        
        # top = int(top * r)
        # right = int(right * r)
        # bottom = int(bottom * r)
        # left = int(left * r)
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Draw a label with a name below the face
        # cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
        # font = cv2.FONT_HERSHEY_DUPLEX
        # cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    # Write the resulting image to the output video file
    print("Writing frame {} / {}".format(frame_number, length))
    output_movie.write(frame)

# All done!
input_movie.release()
cv2.destroyAllWindows()