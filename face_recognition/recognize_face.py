import cv2
import numpy as np
import face_recognition

# Leer las codificaciones de caras desde el archivo encodings.txt
with open('../training/encodings.txt', 'r') as f:
    lines = f.readlines()

encodings = []
names = []
for line in lines:
    encoding_str, name = line.strip().rsplit(',', 1)
    encoding = [float(val) for val in encoding_str.split(',')]
    encodings.append(encoding)
    names.append(name)


# Iniciar la cámara
video_capture = cv2.VideoCapture(0)

while True:
    # Capturar un marco de video
    ret, frame = video_capture.read()

    # Detectar todas las caras en el marco
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Comparar la codificación de la cara detectada con las codificaciones de la base de datos
        matches = face_recognition.compare_faces(encodings, face_encoding)
        distances = face_recognition.face_distance(encodings, face_encoding)
        best_match_index = np.argmin(distances)

        # Si se encontró una coincidencia, mostrar el nombre de la persona en el video
        if matches[best_match_index]:
            name = names[best_match_index]

            # Dibujar un rectángulo alrededor de la cara
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Escribir el nombre de la persona encima del rectángulo
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Mostrar el marco de video resultante
    cv2.imshow('Video', frame)

    # Si se presiona la tecla 'q', salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Liberar la cámara y cerrar todas las ventanas abiertas
video_capture.release()
cv2.destroyAllWindows()

