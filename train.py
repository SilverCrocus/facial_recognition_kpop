import face_recognition
import numpy
import os
import csv


encodings = []
names = []

data_dir = os.listdir("./Pictures/")



for i in range(0, len(data_dir)):
    pictures = os.listdir(f"./Pictures/{data_dir[i]}")


    j = 0
    for img in pictures:
        try:
            if j > 300:
                break
            
            face = face_recognition.load_image_file(f"./Pictures/{data_dir[i]}/{img}")

            face_bounding_boxes = face_recognition.face_locations(face)


            if len(face_bounding_boxes) == 1:
                print(f"{img}...")
                face_enc = face_recognition.face_encodings(face)[0]
                encodings.append(face_enc)
                names.append(data_dir[i])

            else:
                print(f"{data_dir[i]}/{img} was skipped and can't be used for training")

            j += 1
        
        except:
            print(f"{img} was not a picture file")
            j += 1
            continue


numpy.savetxt("encodings.csv", encodings, delimiter = ",")
with open('names.csv', 'w') as result_file:
    wr = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for name in names:
        wr.writerow([name])