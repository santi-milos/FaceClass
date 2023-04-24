from app.camera import Camera
from app.models.people import save_attendance
from app.helpers.face_utils import load_encodings, detect_faces, compare_faces
import cv2

# Cargar las codificaciones de las caras
encodings, names = load_encodings()

# Iniciar la cámara
camera = Camera()

while True:
    # Capturar un marco de video
    frame = camera.get_frame()

    if frame is None:
        continue

    # Detectar todas las caras en el marco
    face_locations, face_encodings = detect_faces(frame)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Comparar la codificación de la cara detectada con las codificaciones de la base de datos
        matches, best_match_index = compare_faces(encodings, face_encoding)

        # Si se encontró una coincidencia, mostrar el nombre de la persona en el video
        if matches[best_match_index]:
            name = names[best_match_index]

            # Guardar el registro en la base de datos
            save_attendance("13-305", "Principios de Desarrollo de software", name, "Mario")

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

camera.stop()
cv2.destroyAllWindows()
