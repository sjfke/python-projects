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
        self.name = name

        if not isinstance(age, int):
            raise TypeError(f"Invalid int for age: {age}")
        if not isinstance(sex, str):
            raise TypeError(f"Invalid str for sex: {sex}")

        if age > 150 or age < 0:
            raise ValueError(f"Invalid age: {age}")
        else:
            self.age = age

        if sex in Person.GENDER:
            self.sex = sex
        else:
            raise ValueError(f"Invalid Gender: {sex}")

        self._uuid1 = str(uuid.uuid1())
        self.__uuid4 = str(uuid.uuid4())

    def __str__(self) -> str:
        """
        String representation
        :return: human-readable representation (str)
        """
        __str = 'Person: '
        __str += str(self.name) + ', '
        __str += str(self.age) + ', '
        __str += str(self.sex) + ', '
        __str += str(self._uuid1)
        return __str

    def __repr__(self) -> str:
        """
        repr() string representation
        :return: programmatic representation (JSON string)
        """
        __str = "{"
        __str += f"'name': '{self.name}', "
        __str += f"'age': '{self.age}', "
        __str += f"'sex': '{self.sex}', "
        __str += f"'_uuid1': '{self._uuid1}'"
        __str += "}"
        return __str
