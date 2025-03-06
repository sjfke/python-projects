from typing import ClassVar
import uuid


class Person:
    GENDER: ClassVar[set] = {'M', 'F', 'N', 'Male', 'Female', 'Neuter'}

    def __init__(self, name: str, age: int, sex: str = 'M') -> None:
        """
        Create person object
        :param name: of person, (str)
        :param age: of person (int)
        :param sex: one of set Gender
        """
        self.__name = name

        if not isinstance(age, int):
            raise TypeError(f"Invalid int for age: {age}")
        if not isinstance(sex, str):
            raise TypeError(f"Invalid str for sex: {sex}")

        if age > 150 or age < 0:
            raise ValueError(f"Invalid age: {age}")
        else:
            self.__age = age

        if sex in Person.GENDER:
            self.__sex = sex
        else:
            raise ValueError(f"Invalid Gender: {sex}")

        self.__uuid1 = str(uuid.uuid1())
        self.__uuid4 = str(uuid.uuid4())

    def __get_name(self) -> str:
        """
        Name Getter
        :return: name of person (str)
        """
        return self.__name

    def __set_name(self, value: str) -> None:
        """
        Name Setter
        :param value: new name of person (str)
        :return: None or TypeError
        """
        if not isinstance(value, str):
            raise TypeError(f"Invalid str for name: {value}")
        else:
            self.__name = value

    def __get_age(self) -> int:
        """
        Age Getter
        :return: age of person (int)
        """
        return self.__age

    def __set_age(self, value: int) -> None:
        """
        Age Setter
        :param value: age of person (integer)
        :return: None, TypeError or ValueError
        """

        if not isinstance(value, int):
            raise TypeError(f"Age must be an int: {value}")
        elif value > 150:
            raise ValueError(f"Invalid age: '{value}'")
        elif value > 0:
            self.__age = value
        else:
            self.__age = 0

    def __get_sex(self) -> str:
        """
        Sex (GENDER) Getter
        :return: Person.GENDER
        """
        return self.__sex

    def __set_sex(self, value: str) -> None:
        """
        Sex (GENDER) Setter
        :param value: gender of person (GENDER element)
        :return: None, TypeError or ValueError
        """
        if not isinstance(value, str):
            raise TypeError(f"Sex must be a str: {value}")
        elif value in Person.GENDER:
            self.__sex = value
        else:
            raise ValueError(f"Invalid Gender: {value}")

    def __get_uuid1(self) -> str:
        """
        UUID Getter
        :return: UUID value (string)
        """
        return self.__uuid1

    def __get_uuid4(self) -> str:
        """
        UUID Getter
        :return: UUID value (string)
        """
        return self.__uuid4

    def __str__(self) -> str:
        """
        String representation
        :return: human-readable representation (str)
        """
        __str = 'Person: '
        __str += str(self.__name) + ', '
        __str += str(self.__age) + ', '
        __str += str(self.__sex) + ', '
        __str += str(self.__uuid1) + ', '
        __str += str(self.__uuid4)
        return __str

    def __repr__(self) -> str:
        """
        repr() string representation
        :return: programmatic representation (JSON string)
        """
        __str = "{"
        __str += f"'name': '{self.__name}', "
        __str += f"'age': '{self.__age}', "
        __str += f"'sex': '{self.__sex}', "
        __str += f"'uuid1': '{self.__uuid1}', "
        __str += f"'uuid4': '{self.__uuid4}'"
        __str += "}"
        return __str

    name = property(fget=__get_name, fset=__set_name, fdel=None, doc='Name of Person')
    age = property(fget=__get_age, fset=__set_age, fdel=None, doc='Age of Person')
    sex = property(fget=__get_sex, fset=__set_sex, fdel=None, doc='Gender of Person')
    uuid1 = property(fget=__get_uuid1, fset=None, fdel=None, doc='UUID1 of Person')
    uuid4 = property(fget=__get_uuid4, fset=None, fdel=None, doc='UUID4 of Person')
