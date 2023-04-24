from datetime import datetime
from database import db


def save_attendance(classroom, subject, name, teacher_name):
    collection = db['attendance']

    # Obtener la fecha y hora actual
    now = datetime.now()

    # Verificar si ya se ha registrado la asistencia de la persona en la misma fecha y aula
    existing_record = collection.find_one({"name": name, "date": now.strftime('%Y-%m-%d'), "classroom": classroom})
    if existing_record:
        # Si ya existe un registro para esta persona en la misma fecha y aula, no se guarda nada
        return

    # Crear un nuevo registro de asistencia con el aula, materia, nombre, fecha y hora
    new = {"classroom": classroom, "subject": subject, "name": name, "teacher_name": teacher_name, "date": now.strftime('%Y-%m-%d'), "time": now.strftime('%H:%M:%S')}

    # Insertar el registro en la colección si no existe un registro previo para la persona en la misma fecha y aula
    collection.insert_one(new)
