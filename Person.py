import os
import uuid


class Person:

    def __init__(self, name, age, sex='M'):
        self.__name = name

        if not isinstance(age, int):
            raise ValueError(f"invalid int for age: '{age}'")
        elif age > 0:
            self.__age = age
        else:
            self.__age = 0

        self.__sex = sex
        self.__uuid = str(uuid.uuid4())

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if not isinstance(value, int):
            raise ValueError(f"invalid int for age: '{value}'")
        elif value > 0:
            self.__age = value
        else:
            self.__age = 0

    def get_sex(self):
        return self.__sex

    def set_sex(self, value):
        self.__sex = value

    def get_uuid(self):
        return self.__uuid

    def __str__(self):
        """ String representation """
        __str = 'Person: '
        __str += str(self.__name) + ', '
        __str += str(self.__age) + ', '
        __str += str(self.__sex) + ', '
        __str += str(self.__uuid)
        return __str

    def __repr__(self):
        """ repr() string representation """
        __str = "{"
        __str += f"'name': {self.__name}, "
        __str += f"'age': {self.__age}, "
        __str += f"'sex': {self.__sex}, "
        __str += f"'uuid': {self.__uuid}"
        __str += "}"
        return __str

    # Python attributes requires, property(fget=None, fset=None, fdel=None, doc=None)
    name = property(get_name, set_name, None, None)
    age = property(get_age, set_age, None, None)
    sex = property(get_sex, set_sex, None, None)
    uuid = property(get_uuid, None, None, None)
