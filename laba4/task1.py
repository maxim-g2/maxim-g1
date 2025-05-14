import sqlite3


db_connection = sqlite3.connect("task1.db")

create_tables_sql = """
create table if not exists grades(
id integer primary key,
student_id int references student(id),
grade int not null check(grade between 2 and 5)
);

create table if not exists student(
id integer primary key,
name char(26) not null,
surname char(26) not null,
lastname char(26) not null,
group_number int not null
);
"""

db_connection.executescript(create_tables_sql)
db_connection.commit()


class Student:
    @staticmethod
    def create_from_db_row(db_row, grades=None):
        return Student(db_row[0], db_row[1], db_row[2], db_row[3], db_row[4], grades,
                       db_row[5] if len(db_row) >= 6 else None)

    @staticmethod
    def create_list_from_db(rows):
        return list(map(lambda x: Student.create_from_db_row(x), rows))

    def __init__(self, student_id: int, first_name: str, family_name: str, patronymic: str, group_num: int,
                 marks: [int] = None,
                 avg_mark: int = None):
        self.student_id = student_id
        self.first_name = first_name
        self.family_name = family_name
        self.patronymic = patronymic
        self.group_num = group_num
        self.avg_mark = avg_mark
        self.marks = marks

        if marks is not None:
            self.validate_marks()
            self.calculate_avg_mark()

    def display_info(self):
        print(
            f"ID: {self.student_id}; ФИО: {self.family_name} {self.first_name} {self.patronymic}; Группа: {self.group_num}")

        if self.avg_mark is not None:
            print("Средний балл:", round(self.avg_mark, 2))
        if self.marks is not None:
            print("Оценки:", *self.marks)

    def calculate_avg_mark(self):
        self.avg_mark = sum(self.marks) / len(self.marks)

    def validate_marks(self):
        if len(self.marks) != 4:
            raise ValueError("Должно быть 4 оценки!")

        for mark in self.marks:
            if mark not in (2, 3, 4, 5):
                raise ValueError("Оценки должны быть от 2 до 5!")


def add_new_student(student):
    cursor = db_connection.cursor()
    cursor.execute("insert into student values (null, ?, ?, ?, ?)",
                   (student.first_name, student.family_name, student.patronymic, student.group_num))

    new_student_id = cursor.lastrowid

    student_ids = [new_student_id for b in range(len(student.marks))]
    marks_data = zip(student_ids, student.marks)

    cursor.executemany("insert into grades values (null, ?, ?)", marks_data)
    db_connection.commit()


def show_all_students():
    cursor = db_connection.cursor()
    cursor.execute("select * FROM student")
    students = Student.create_list_from_db(cursor.fetchall())

    print("\nВсе студенты:")
    if not students:
        print("Нет данных")
        return

    for student in students:
        student.display_info()


def show_student_details():
    cursor = db_connection.cursor()

    student_id = int(input("ID студента: "))

    cursor.execute("select * FROM student WHERE id=?", (student_id,))
    student_data = cursor.fetchone()

    if not student_data:
        print("Студент не найден")
        return

    cursor.execute("select grade FROM grades WHERE student_id=?", (student_id,))
    marks_data = cursor.fetchall()
    marks = tuple(zip(*marks_data))[0] if marks_data else []

    student = Student.create_from_db_row(student_data, marks)
    print("\nИнформация о студенте:")
    student.display_info()


def update_student_info():
    cursor = db_connection.cursor()

    student_id = int(input("ID студента для изменения: "))

    cursor.execute("select * FROM student WHERE id=?", (student_id,))
    student_data = cursor.fetchone()

    if not student_data:
        print("Студент не найден")
        return

    cursor.execute("select id, grade from grades where student_id=?", (student_id,))
    grades_data = cursor.fetchall()
    grade_ids, current_marks = tuple(zip(*grades_data)) if grades_data else ([], [])

    student = Student.create_from_db_row(student_data, current_marks)

    print("\nТекущие данные студента:")
    student.display_info()

    print("\nВведите новые данные (оставьте пустым для сохранения текущих):")

    new_first_name = input("Имя: ")
    new_family_name = input("Фамилия: ")
    new_patronymic = input("Отчество: ")
    new_group_num = input("Группа: ")
    new_marks = input("Оценки (4 оценки через пробел): ")

    try:
        if new_marks:
            new_marks = list(map(int, new_marks.split()))
            if len(new_marks) != 4 or any(mark not in (2, 3, 4, 5) for mark in new_marks):
                raise ValueError("Некорректные оценки")

        if new_group_num:
            new_group_num = int(new_group_num)
    except ValueError:
        print("Ошибка в данных группы или оценок")
        return

    if new_marks:
        cursor.executemany("update grades set grade=? where id=?", zip(new_marks, grade_ids))

    if new_first_name:
        cursor.execute("update student set name=? where id=?", (new_first_name, student_id))
    if new_family_name:
        cursor.execute("update student set surname=? where id=?", (new_family_name, student_id))
    if new_patronymic:
        cursor.execute("update student set lastname=? where id=?", (new_patronymic, student_id))
    if new_group_num:
        cursor.execute("update student set group_number=? where id=?", (new_group_num, student_id))

    print("Изменения сохранены!")
    db_connection.commit()


def remove_student():
    cursor = db_connection.cursor()

    student_id = int(input("ID студента для удаления: "))

    cursor.execute("delete FROM grades WHERE student_id=?", (student_id,))
    cursor.execute("delete FROM student WHERE id=?", (student_id,))

    print("Студент удален!" if cursor.rowcount else "Студент не найден")
    db_connection.commit()


def show_group_avg_marks():
    cursor = db_connection.cursor()

    group_num = int(input("Номер группы: "))

    cursor.execute(
        """
        select student.id, student.name, student.surname, student.lastname, 
               student.group_number, AVG(grade) 
        FROM student 
        INNER JOIN grades ON student.id = grades.student_id
        WHERE group_number = ? 
        GROUP BY student.id 
        """, (group_num,))

    group_students = Student.create_list_from_db(cursor.fetchall())

    print(f"\nСредние баллы группы {group_num}:")

    if not group_students:
        print("Нет данных")
        return

    for student in group_students:
        student.display_info()


def main_menu():
    while True:
        print("\nГлавное меню:")
        print("1. Добавить нового студента")
        print("2. Показать всех студентов")
        print("3. Показать информацию о студенте")
        print("4. Изменить данные студента")
        print("5. Удалить студента")
        print("6. Показать средние баллы по группе")
        print("0. Выход")

        try:
            choice = int(input("Выберите действие: "))
        except ValueError:
            print("Введите число!")
            continue

        print()

        if choice == 1:
            first_name = input("Имя: ")
            family_name = input("Фамилия: ")
            patronymic = input("Отчество: ")
            group_num = int(input("Номер группы: "))
            marks = list(map(int, input("Оценки (4 оценки через пробел): ").split()))

            try:
                new_student = Student(-1, first_name, family_name, patronymic, group_num, marks)
                add_new_student(new_student)
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == 2:
            show_all_students()
        elif choice == 3:
            show_student_details()
        elif choice == 4:
            update_student_info()
        elif choice == 5:
            remove_student()
        elif choice == 6:
            show_group_avg_marks()
        elif choice == 0:
            break
        else:
            print("Неверный выбор")

        input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main_menu()
    db_connection.close()