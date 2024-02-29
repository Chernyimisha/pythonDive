
class Student:

    def __init__(self, name: str, subjects_file: str):
        self.name = name
        self.subjects = self.load_subjects(subjects_file)

    def check_subjects(self, subject: str):
        subjects = ['Математика', 'Физика', 'История', 'Литература']
        if subject in subjects:
            return True
        else:
            raise ValueError(f'Предмет {subject} не найден')

    def load_subjects(self, subjects_file: str):
        res = {}
        with open(subjects_file, 'r', encoding='utf-8') as src:
            data = src.read().split(',')
        for item in data:
            if self.check_subjects(item):
                res[item] = {}
            else:
                print(f'Предмет {item} не найден')
        return res

    def add_grade(self, subject, grade):
        if self.check_subjects(subject):
            if isinstance(grade, int) and (2 <= grade <= 5):
                if 'Оценки' in self.subjects[subject]:
                    self.subjects[subject]['Оценки'].append(grade)
                else:
                    self.subjects[subject]['Оценки'] = [grade]
            else:
                print('Оценка должна быть целым числом от 2 до 5')

    def add_test_score(self, subject, test_score):
        if self.check_subjects(subject):
            if isinstance(test_score, int) and (0 <= test_score <= 100):
                if 'Результаты тестов' in self.subjects[subject]:
                    self.subjects[subject]['Результаты тестов'].append(test_score)
                else:
                    self.subjects[subject]['Результаты тестов'] = [test_score]
            else:
                print('Результат теста должен быть целым числом от 0 до 100')

    def get_average_test_score(self, subject):
        if self.check_subjects(subject):
            return round(sum(self.subjects[subject]['Результаты тестов']) /
                         len(self.subjects[subject]['Результаты тестов']), 1)

    def get_average_grade(self):
        count = 0
        sum_grade = 0
        for v in self.subjects.values():
            if 'Оценки' in v:
                sum_grade += sum(v['Оценки'])
                count += len(v['Оценки'])
        return round(sum_grade / count, 1)

    def __setattr__(self, name, value):
        if name == 'name' and (len(value.split()) != sum([int(i.isalpha()) for i in value.split()])
                               or len(value.split()) != sum([int(i == i.capitalize()) for i in value.split()])):
            print('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        else:
            object.__setattr__(self, name, value)

    def __getattr__(self, name):
        return self.subjects[name]

    def __str__(self):
        return f'Студент: {self.name}\nПредметы: {", ".join([k for k, v in self.subjects.items() if v != {}])}'


if __name__ == '__main__':
    # student = Student("Иван Иванов", "subjects.csv")

    # student.add_grade("Математика", 4)
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
    # student = Student("Петров Петр", "subjects.csv")
    student = Student("123 Иван", "subjects.csv")

    # student.add_grade("Физика", 6)

    # print(student)

