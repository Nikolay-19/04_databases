import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries

from main_app.models import Student

students = Student.objects.all()


def add_students():
    a = Student(
        student_id="FC5204", first_name="John", last_name="Doe", birth_date="1995-05-15",
        email="john.doe@university.com")
    b = Student(
        student_id="FE0054", first_name="Jane", last_name="Smith", birth_date=None, email="jane.smith@university.com")
    c = Student(
        student_id="FH2014", first_name="Alice", last_name="Johnson", birth_date="1998-02-10",
        email="alice.johnson@university.com")
    d = Student(
        student_id="FH2015", first_name="Bob", last_name="Wilson", birth_date="1996-11-25",
        email="bob.wilson@university.com")

    a.save()
    b.save()
    c.save()
    d.save()


# add_students()
# print(Student.objects.all())


def get_students_info():
    result = []
    for student in students:
        result.append(
            f"Student №{student.student_id}: {student.first_name} {student.last_name}; Email: {student.email}")

    return "\n".join(str(el) for el in result)


# print(get_students_info())

def update_students_emails():
    for student in students:
        student.email = student.email.replace("university.com", "uni-students.com")
        student.save()


# update_students_emails()
# print([el.email for el in students])

def truncate_students():
    students.delete()


# truncate_students()
# print(students)
# print(f"Number of students: {students.count()}")
