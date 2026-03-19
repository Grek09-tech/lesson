# Полные классы (из предыдущих заданий)
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self.get_avg_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}"

    def get_avg_grade(self):
        if not self.grades:
            return 0
        total = sum(sum(course_grades) for course_grades in self.grades.values())
        count = sum(len(course_grades) for course_grades in self.grades.values())
        return total / count if count > 0 else 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer): return NotImplemented
        return self.get_avg_grade() < other.get_avg_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer): return NotImplemented
        return self.get_avg_grade() > other.get_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer): return NotImplemented
        return self.get_avg_grade() == other.get_avg_grade()

class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Student:
    def __init__(self, surname, name, gender):
        self.surname = surname
        self.name = name
        self.gender = gender
        self.courses_in_progress = []
        self.finished_courses = []
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        avg_homework = self.get_avg_homework_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_homework:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def get_avg_homework_grade(self):
        if not self.grades: return 0
        total = sum(sum(course_grades) for course_grades in self.grades.values())
        count = sum(len(course_grades) for course_grades in self.grades.values())
        return total / count if count > 0 else 0

    def __lt__(self, other):
        if not isinstance(other, Student): return NotImplemented
        return self.get_avg_homework_grade() < other.get_avg_homework_grade()

    def __gt__(self, other):
        if not isinstance(other, Student): return NotImplemented
        return self.get_avg_homework_grade() > other.get_avg_homework_grade()

    def __eq__(self, other):
        if not isinstance(other, Student): return NotImplemented
        return self.get_avg_homework_grade() == other.get_avg_homework_grade()

    def rate_lecture(self, lecturer, course, grade):
        if (not isinstance(lecturer, Lecturer) or 
            course not in self.courses_in_progress or 
            course not in lecturer.courses_attached):
            return "Ошибка"
        if course not in lecturer.grades:
            lecturer.grades[course] = []
        lecturer.grades[course].append(grade)
        return None


# Создаем по 2 экземпляра каждого класса
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Пётр', 'Петров')
reviewer1 = Reviewer('Анна', 'Смирнова')
reviewer2 = Reviewer('Мария', 'Козлова')
student1 = Student('Алёхина', 'Ольга', 'Ж')
student2 = Student('Петров', 'Дмитрий', 'М')

# Настраиваем курсы и оценки
student1.courses_in_progress = ['Python']
student2.courses_in_progress = ['Python', 'Java']
lecturer1.courses_attached = ['Python']
lecturer2.courses_attached = ['Python', 'Java']

# Вызываем методы
student1.rate_lecture(lecturer1, 'Python', 8)
student1.rate_lecture(lecturer1, 'Python', 9)
student2.rate_lecture(lecturer2, 'Python', 7)
student2.rate_lecture(lecturer2, 'Java', 10)

# Выводим все объекты
print("=== ЛЕКТОРЫ ===")
print(lecturer1)
print(lecturer2)
print(lecturer1 > lecturer2)  # True (8.5 > 8.5? Нет, но для примера)

print("\n=== РЕВЬЮЕРЫ ===")
print(reviewer1)
print(reviewer2)

print("\n=== СТУДЕНТЫ ===")
print(student1)
print(student2)
print(student1 < student2)  # False

# Функции для подсчета средних оценок
def avg_students_homework(students_list, course):
    """Средняя оценка за ДЗ по курсу для всех студентов"""
    total_grades = []
    for student in students_list:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    return round(sum(total_grades) / len(total_grades), 1) if total_grades else 0

def avg_lecturers_rating(lecturers_list, course):
    """Средняя оценка за лекции по курсу для всех лекторов"""
    total_grades = []
    for lecturer in lecturers_list:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    return round(sum(total_grades) / len(total_grades), 1) if total_grades else 0

# Тестируем функции
students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print("\n=== СРЕДНИЕ ОЦЕНКИ ===")
print(f"Средняя оценка студентов за Python: {avg_students_homework(students, 'Python')}")
print(f"Средняя оценка лекторов за Python: {avg_lecturers_rating(lecturers, 'Python')}")
print(f"Средняя оценка лекторов за Java: {avg_lecturers_rating(lecturers, 'Java')}")
