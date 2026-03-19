class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # словарь {курс: [оценки]}

class Reviewer(Mentor):
    pass

class Student:
    def __init__(self, surname, name, gender):
        self.surname = surname
        self.name = name
        self.gender = gender
        self.courses_in_progress = []
        self.finished_courses = []
        self.courses_attached = []
        # ... другие атрибуты при необходимости

    def rate_lecture(self, lecturer, course, grade):
        # Проверяем, что лектор закреплен за курсом
        if course not in lecturer.courses_attached:
            return f"Ошибка"
        
        # Проверяем, что студент изучает этот курс
        if course not in self.courses_in_progress:
            return f"Ошибка"
        
        # Проверяем, что это Lecturer (не Reviewer)
        if not isinstance(lecturer, Lecturer):
            return f"Ошибка"
        
        # Добавляем оценку
        if course not in lecturer.grades:
            lecturer.grades[course] = []
        lecturer.grades[course].append(grade)
        return None

# Тест
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))   # None
print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))      # Ошибка  
print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка

print(lecturer.grades)  # {'Python': [7]}
