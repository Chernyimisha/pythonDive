
class Student:

    def __init__(self, name: str, subjects_file: str):
        self.name = name
        self.subjects = self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file: str):
        res = {}
        with open(subjects_file, 'r', encoding='utf-8') as src:
            data = src.read().split(',')
        for item in data:
            res[item] = {}
        return res

    def add_grade(self, subject, grade):
        if isinstance(grade, int) and (2 <= grade <= 5):
            self.subjects[subject]['Оценки'] = grade

    # def add_test_score(self, subject, test_score):
    #     pass

    # def get_average_test_score(self, subject):
    #     pass
    #
    # def get_average_grade(self):
    #     pass

    # def __setattr__(self, name, value):
    #     pass

    def __getattr__(self, name):
        return self.subjects[name]

    def __str__(self):
        return f'Студент: {self.name}\nПредметы: {", ".join([key for key in self.subjects.keys()])}'


if __name__ == '__main__':

    student = Student("Иван Иванов", "subjects.csv")

    student.add_grade("Математика", 4)
    print(student.__getattr__("Математика"))
    # student.add_test_score("Математика", 85)
    #
    # student.add_grade("История", 5)
    # student.add_test_score("История", 92)
    #
    # average_grade = student.get_average_grade()
    # print(f"Средний балл: {average_grade}")
    #
    # average_test_score = student.get_average_test_score("Математика")
    # print(f"Средний результат по тестам по математике: {average_test_score}")

    print(student)

