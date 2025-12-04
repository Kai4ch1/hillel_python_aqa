from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, Mapped
from faker import Faker
import random

faker = Faker()
Base = declarative_base()

engine = create_engine('sqlite:///students.db', echo=True)

common_table = Table("associate_table", Base.metadata,
                     Column("student_id", Integer, ForeignKey("students.student_id")),
                     Column("course_id", Integer, ForeignKey("courses.course_id")))

class Student(Base):
    __tablename__ = 'students'

    student_id: Mapped[int] = Column(
        Integer,
        primary_key=True
    )
    student_name = Column(
        String,
        unique=True
    )
    courses = relationship("Course", secondary=common_table, back_populates="students")

    def __repr__(self) -> str:
        return (f"student_name={self.student_name}, "
                f"id of student={self.student_id}, "
                f"courses={self.courses}")


class Course(Base):
    __tablename__ = 'courses'

    course_id: Mapped[int] = Column(
        Integer,
        primary_key=True
    )
    course_name = Column(
        String,
        unique=True
    )
    students = relationship("Student", secondary=common_table,  back_populates="courses")

    def __repr__(self) -> str:
        return (f"course_id={self.course_id}, "
                f"course name={self.course_name}, "
                f"students={self.students}")

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)

session = SessionLocal()


def new_student_and_course(student: str, course: str) -> None:
    create_user = Student(student_name=student)

    existing_course = session.query(Course).filter(Course.course_name == course).first()
    if existing_course:
        add_course = existing_course
    else:
        add_course = Course(course_name=course)

    create_user.courses.append(add_course)
    session.add(add_course)

    session.add(create_user)
    session.commit()



if __name__ == "__main__":
    courses_list = ["C-- Start", "C# Start", "C Start", "Python", "C-- start"]
    # створення 20 студентів із записом на рандомний курс
    #for _ in range(20):
    #    random_course = random.choice(courses_list)
    #    new_student_and_course(faker.name(), random_course)

    #retrieve the list of students
    list_of_students_query = session.query(Student).filter(Student.courses.any(Course.course_name == "Python")).all()
    for student in list_of_students_query:
        print("Students on course=", student)

    #retrieve the student from the course
    find_student_via_course = session.query(Course).filter(Course.students.any(Student.student_name == "Paul")).all()
    for course in find_student_via_course:
        print("Courses of seeking student=", course.course_name)

    # fetch the student:
    find_single_student = session.query(Student).filter(Student.student_name == "Paul").first()

    # modify the student:
    if find_single_student:
        find_single_student.student_name = "Pavel Pavel"
        print("Updated, student =", find_single_student)
        session.commit()
    else:
        print("Student does not exists")

    # delete student
    if find_single_student:
        session.delete(find_single_student)
        print(f"student {find_single_student} was successfully deleted")
        session.commit()

    else:
        print("Student was not found")