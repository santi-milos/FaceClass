import os
import numpy as np
import face_recognition


# Leer las codificaciones de caras desde el archivo encodings.txt
def load_encodings():
    encodings_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'training', 'encodings.txt'))

    with open(encodings_path) as f:
        lines = f.readlines()

    encodings = []
    names = []
    for line in lines:
        encoding_str, name = line.strip().rsplit(',', 1)
        encoding = [float(val) for val in encoding_str.split(',')]
        encodings.append(encoding)
        names.append(name)

    return encodings, names


# Detectar todas las caras en el marco
def detect_faces(frame):
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    return face_locations, face_encodings


# Comparar la codificación de la cara detectada con las codificaciones de la base de datos
def compare_faces(encodings, face_encoding):
    matches = face_recognition.compare_faces(encodings, face_encoding)
    distances = face_recognition.face_distance(encodings, face_encoding)
    best_match_index = np.argmin(distances)
    return matches, best_match_index
