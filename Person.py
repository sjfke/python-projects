import os
import uuid


class Person:

    def __init__(self, name, age, sex='M'):
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__uuid = str(uuid.uuid4())

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value

    def get_sex(self):
        return self.__sex

    def set_sex(self, value):
        self.__sex = value

    def get_uuid(self):
        return self.__uuid

    def __str__(self):
        """ String representation """
        __str = ''
        __str += str(self.__name) + ', '
        __str += str(self.__age) + ', '
        __str += str(self.__sex) + ', '
        __str += str(self.__uuid)
        return __str

    def __repr__(self):
        """ YAML like string representation """
        __str = ''
        __str += "{0}: {1}".format('name', self.__name) + os.linesep
        __str += "{0}: {1}".format('age', self.__age) + os.linesep
        __str += "{0}: {1}".format('sex', self.__sex) + os.linesep
        __str += "{0}: {1}".format('uuid', self.__uuid)
        return __str
