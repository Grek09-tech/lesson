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
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_avg_grade() < other.get_avg_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_avg_grade() > other.get_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_avg_grade() == other.get_avg_grade()


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"  # Без лишнего переноса


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
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_homework:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def get_avg_homework_grade(self):
        if not self.grades:
            return 0
        total = sum(sum(course_grades) for course_grades in self.grades.values())
        count = sum(len(course_grades) for course_grades in self.grades.values())
        return total / count if count > 0 else 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_avg_homework_grade() < other.get_avg_homework_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_avg_homework_grade() > other.get_avg_homework_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
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

reviewer = Reviewer('Some', 'Buddy')
lecturer = Lecturer('Some', 'Buddy')
lecturer.grades = {'Python': [99]}

student = Student('Eman', 'Ruoy', 'M')
student.courses_in_progress = ['Python', 'Git']
student.finished_courses = ['Введение в программирование']
student.grades = {'Python': [99]}

print(reviewer)
# Имя: Some
# Фамилия: Buddy

print(lecturer)  
# Имя: Some
# Фамилия: Buddy
# Средняя оценка за лекции: 9.9

print(student)
# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.9
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование
