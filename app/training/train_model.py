import os
import cv2
import face_recognition

# Carga todas las imágenes de la base de datos
base_path = '../database'
person_folders = os.listdir(base_path)
image_paths = []
for person_folder in person_folders:
    person_path = os.path.join(base_path, person_folder)
    if os.path.isdir(person_path):
        for image_filename in os.listdir(person_path):
            image_path = os.path.join(person_path, image_filename)
            image_paths.append(image_path)

# Carga las imágenes y codifica las caras en la base de datos
encodings = []
names = []
for image_path in image_paths:
    image = cv2.imread(image_path)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    face_encodings = face_recognition.face_encodings(rgb_image)
    if len(face_encodings) > 0:
        encodings.append(face_encodings[0])
        names.append(os.path.basename(os.path.dirname(image_path)))

# Guarda las codificaciones de cara en un archivo
with open('encodings.txt', 'w') as f:
    for i in range(len(names)):
        encoding_str = ','.join([str(val) for val in encodings[i]])
        f.write(f'{encoding_str},{names[i]}\n')
