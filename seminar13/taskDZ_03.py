
class MyError(Exception):
    pass


class InvalidNameError(MyError):
    pass


class InvalidAgeError(MyError):
    pass


class InvalidIdError(MyError):
    pass


def validate_text(value):
    if not isinstance(value, str) or value == '':
        raise InvalidNameError(f'Invalid name: {value}. Name should be a non-empty string.')


def validate_age(value):
    if not isinstance(value, int) or value <= 0:
        raise InvalidAgeError(f'Invalid age: {value}. Age should be a positive integer.')


def validate_id(value):
    if not isinstance(value, int) or len([j for j in list(str(value))]) != 6:
        raise InvalidIdError(f'Invalid id: {value}. Id should be a 6-digit positive integer between 100000 and 999999.')


class MyStr(str):
    def __init__(self, value=''):
        self.value = value

    def __set__(self, instance, value):
        validate_text(value)
        setattr(instance, self.value, value)


class Person:

    last_name = MyStr()
    first_name = MyStr()
    free_name = MyStr()

    def __init__(self, last_name, first_name, free_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.free_name = free_name
        validate_age(age)
        self.age = age

    def __setattr__(self, key, value):
        if key == 'age':
            validate_age(value)
        object.__setattr__(self, key, value)

    def birthday(self):
        self.age += 1
        return self.age

    def get_age(self):
        return self.age

    def get_last_name(self):
        return self.last_name

    def get_first_name(self):
        return self.first_name

    def get_free_name(self):
        return self.free_name


class Employee(Person):
    def __init__(self, last_name, first_name, free_name, age, id_number):
        validate_id(id_number)
        super().__init__(last_name, first_name, free_name, age)
        self.id = id_number

    def get_level(self):
        return (sum([int(j) for j in list(str(self.id))])) % 7

    def __setattr__(self, key, value):
        if key == "id_number":
            validate_id(value)
        object.__setattr__(self, key, value)


if __name__ == '__main__':
    # person1 = Person("", "John", "Doe", 30)
    # person2 = Person("Alice", "Smith", "Johnson", -5)
    person = Person("Alice", "Smith", "Johnson", -5)
    # employee = Employee("Bob", "Johnson", "Brown", 40, 12345)
    # person2 = Person("Alice", "Smith", "Johnson", 25)
    # print(person2.get_age())


