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
        """
        Getter Name
        :return: name of person
        :rtype: str
        """
        return self.__name

    def set_name(self, value):
        """
        Setter name
        :param value: name of person
        :type value: str
        :return: None
        :rtype: NoneType
        """
        self.__name = value

    def get_age(self):
        """
        Getter age
        :return: age of person
        :rtype: int
        """
        return self.__age

    def set_age(self, value):
        """
        Setter age
        :param value: age of person
        :type value: int
        :return: None
        :rtype: NoneType
        """
        if not isinstance(value, int):
            raise ValueError(f"invalid int for age: '{value}'")
        elif value > 0:
            self.__age = value
        else:
            self.__age = 0

    def get_sex(self):
        """
        Getter gender
        :return: gender of person
        :rtype: str
        """
        return self.__sex

    def set_sex(self, value):
        """
        Setter gender
        :param value: gender of person ('M', 'F', 'N')
        :type value: str
        :return: None
        :rtype: NoneType
        """
        self.__sex = value

    def get_uuid(self):
        """
        Getter uuid
        :return:UUID value
        :rtype: str
        """
        return self.__uuid

    def __str__(self):
        """
        String representation
        :return: human readable representation
        :rtype: str
        """
        __str = 'Person: '
        __str += str(self.__name) + ', '
        __str += str(self.__age) + ', '
        __str += str(self.__sex) + ', '
        __str += str(self.__uuid)
        return __str

    def __repr__(self):
        """
        repr() string representation
        :return: programmatic representation
        :rtype: str
        """
        __str = "{"
        __str += f"'name': '{self.__name}', "
        __str += f"'age': {self.__age}, "
        __str += f"'sex': '{self.__sex}', "
        __str += f"'uuid': '{self.__uuid}'"
        __str += "}"
        return __str

    # Python attributes requires, property(fget=None, fset=None, fdel=None, doc=None)
    name = property(get_name, set_name, None, None)
    age = property(get_age, set_age, None, None)
    sex = property(get_sex, set_sex, None, None)
    uuid = property(get_uuid, None, None, None)
