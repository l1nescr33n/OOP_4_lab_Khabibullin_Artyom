from random import choice

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    class Student:
        """
        Документация на класс.
        Класс выводит основную информацию о поступающем студенте.
        """
        def __init__(self, locality: str, school_number: int, profile: str):
            self._locality = locality
            self._school_number = school_number
            self._profile = profile
        """
        Создание и подготовка к работе объекта 'Студент'
        
        :param _locality: место проживания студента по прописке
        :param _school_number: номер школы
        :param _profile: профиль обучения
        
        Примеры:
        >>> new_student = Student("г. Санкт-Петербург", 186, "гум")
        """

        """Инициализация экземпляра класса"""
        @property
        def get_locality(self):  # Получение информации о прописке
            return self._locality

        @get_locality.setter
        def get_locality(self, _locality):  # Проверка на то, что данные получены
            if type(self._locality) is not str:
                raise TypeError("напишите название города")

        @property
        def get_school_number(self) -> int:  # Проверка получения данных о школе
            return self._school_number

        @get_school_number.setter
        def get_school_number(self, _school_number: int):  # Проверка значения номера школы
            if type(_school_number) is not int:  # Проверка типа целочисленного
                raise TypeError("номер школы - целое число")
            if _school_number < 0:  # Проверка на положительность
                raise ValueError("номер школы должен быть больше 0")

        """
        Проверка места прописки в Санкт-Петербурге.
        Метод перегружается в дочерних классах.
        
        :return: Есть ли нужда в общежитии
        
        Примеры:
        
        >>> need_in_dorm = Student("г. Санкт-Петербург", 186, "гум")
        >>> need_in_dorm.need_dorm()
        """
        def need_dorm(self) -> None:
            if self._locality == "г. Санкт-Петербург":
                # Если прописка в Петербурге, то программа выводит отсутствие нужды в общежитии
                return print("Не нуждается в общежитии")
            else:
                # Если нет, то программа выводит, что нужда в общежитии есть
                return print("Нуждается в общежитии")

        """
        Функция проверяет на наличие олимпиад.
        Метод в дочерних классах наследуется.
        
        :return: "Олимпиадник"/"Достижений нет"
        
        Примеры:
        
        >>> new_student = Student("г. Санкт-Петербург", 186, "гум")
        >>> new_student.has_olympiads()
        """
        @staticmethod
        def has_olympiads() -> None:  # Метод выводит информацию о наличии побед в олимпиадах
            olympiads = choice([True, False])
            if olympiads is True:
                return print("Олимпиадник")
            else:
                return print("Достижений нет")

        """
        Метод выводит информацию о студенте в "официальном" представлении
        """
        def __repr__(self) -> None:
            return print(f'Student(locality={self._locality}, school number={self._school_number}, profile={self._profile})')
        """
        Метод выводит информацию о студенте в "удобочитаемом" представлении
        """
        def __str__(self):
            return f'профиль {self._profile}, населённый пункт {self._locality}, номер школы {self._school_number}'

    class Technical(Student):
        """
        Документация на класс.
        Дополняет информацию о студенте технического направления и баллах за его экзамены
        """
        def __init__(self, locality: str, school_number: int, math: int, physics: int):
            super().__init__(locality, school_number, profile="тех")
            self._math = math
            self._physics = physics

        """
        Создание и подготовка к работе объекта 'Technical'
        
        :param _math: количество баллов за экзамен по математике
        :param _physics: количество баллов за экзамен по физике
        
        >>> technical_student = Technical("г. Тверь, 619, 100, 87")
        """
        @property
        def get_math_results(self) -> int:  # Проверка на правильный ввод результатов экзамена по математике
            return self._math

        @get_math_results.setter
        def get_math_results(self, _math: int):
            if self._math is not int:
                raise TypeError("результат теста должен быть целым числом")
            if 0 > self._math or 100 < self._math:
                raise ValueError("результат теста должен быть в диапазоне от 0 до 100")

        @property
        def get_physics_results(self) -> int:  # Проверка на правильный ввод результатов экзамена по физике
            return self._physics

        @get_physics_results.setter
        def get_physics_results(self, _physics: int):
            if self._physics is not int:
                raise TypeError("результат теста должен быть целым числом")
            if 0 > self._physics or 100 < self._physics:
                raise ValueError("результат теста должен быть в диапазоне от 0 до 100")

        """
        Проверка места прописки в Санкт-Петербурге и нужного количества баллов

        :return: Есть ли нужда в общежитии

        Примеры:

        >>> need_in_dorm = Technical("г. Екатеринбург", 1, 82, 56)
        >>> need_in_dorm.need_dorm()
        """
        def need_dorm(self) -> None:
            if self._locality == "г. Санкт-Петербург" or self._math + self._physics < 120:
                print("Не нуждается в общежитии")
            else:
                print("Нуждается в общежитии")

        """
        Метод выводит информацию о студенте в "официальном" представлении
        """
        def __repr__(self) -> str:
            return f'Technical(region={self._locality}, school number={self._school_number}, profile={self._profile}, physics={self._physics}, math={self._math})'

    class Economical(Student):
        """
        Документация на класс.
        Дополняет информацию о студенте экономического направления и баллах за его экзамены
        """
        def __init__(self, locality: str, school_number: int, economics: int, law: int):
            super().__init__(locality, school_number, profile="соц-эк")
            self._economics = economics
            self._law = law

        """
        Создание и подготовка к работе объекта 'Economical'

        :param _economics: количество баллов за экзамен по экономике
        :param _law: количество баллов за экзамен по праву

        >>> economical_student = Economical("г. Новосибирск", 110, 60, 77)
        """
        @property
        def get_economics_results(self) -> int: # Проверка на правильный ввод результатов экзамена по экономике
            return self._economics

        @get_economics_results.setter
        def get_economics_results(self, _economics: int):
            if self._economics is not int:
                raise TypeError("результат теста должен быть целым числом")
            if 0 > self._economics or 100 < self._economics:
                raise ValueError("результат теста должен быть в диапазоне от 0 до 100")

        @property
        def get_law_results(self) -> int: # Проверка на правильный ввод результатов экзамена по праву
            return self._law

        @get_law_results.setter
        def get_law_results(self, _law: int):
            if self._law is not int:
                raise TypeError("результат теста должен быть целым числом")
            if 0 > self._law or 100 < self._law:
                raise ValueError("результат теста должен быть в диапазоне от 0 до 100")

        """
        Проверка места прописки в Санкт-Петербурге и нужного количества баллов

        :return: Есть ли нужда в общежитии

        Примеры:

        >>> need_in_dorm = Economical("г. Новосибирск", 110, 60, 77)
        >>> need_in_dorm.need_dorm()
        """
        def need_dorm(self) -> None:
            if self._locality == "г. Санкт-Петербург" or self._law + self._economics < 120:
                print("Не нуждается в общежитии")
            else:
                print("Нуждается в общежитии")

        """
        Метод выводит информацию о студенте в "официальном" представлении
        """
        def __repr__(self) -> str:
            return f'Economical(region={self._locality}, school number={self._school_number}, profile={self._profile}, economics={self._economics}, law={self._law})'


    class Humanitarian(Student):
        """
        Документация на класс.
        Дополняет информацию о студенте гуманитарного направления и баллах за его экзамены
        """
        def __init__(self, locality: str, school_number: int, english: int, literature: int):
            super().__init__(locality, school_number, profile="гум")
            self._english = english
            self._literature = literature

        """
        Создание и подготовка к работе объекта 'Economical'

        :param _english: количество баллов за экзамен по английскому языку
        :param _literature: количество баллов за экзамен по литературе

        >>> humanitarian_student = Humanitarian("г. Краснодар", 69, 90, 88)
        """
        @property
        def get_english_results(self) -> int:  # Проверка на правильный ввод результатов экзамена по английскому языку
            return self._english

        @get_english_results.setter
        def get_english_results(self, _english: int):
            if self._english is not int:
                raise TypeError("результат теста должен быть целым числом")
            if 0 > self._english or 100 < self._english:
                raise ValueError("результат теста должен быть в диапазоне от 0 до 100")

        @property
        def get_literature_results(self) -> int:  # Проверка на правильный ввод результатов экзамена по литературе
            return self._literature

        @get_literature_results.setter
        def get_literature_results(self, _literature: int):
            if self._literature is not int:
                raise TypeError("результат теста должен быть целым числом")
            if 0 > self._literature or 100 < self._literature:
                raise ValueError("результат теста должен быть в диапазоне от 0 до 100")

        """
        Проверка места прописки в Санкт-Петербурге и нужного количества баллов

        :return: Есть ли нужда в общежитии

        Примеры:

        >>> need_in_dorm = Humanitarian("г. Краснодар", 69, 90, 88)
        >>> need_in_dorm.need_dorm()
        """
        def need_dorm(self) -> None:
            if self._locality == "г. Санкт-Петербург" or self._literature + self._english < 120:
                return print("Не нуждается в общежитии")
            else:
                return print("Нуждается в общежитии")

        """
        Метод выводит информацию о студенте в "официальном" представлении
        """
        def __repr__(self) -> str:
            return f'Humanitarian(region={self._locality}, school number={self._school_number}, profile={self._profile}, english={self._english}, literature={self._literature})'

    students_data = Economical("г. Москва", 228, 92, 89).__repr__()
    dorm_need = Technical("г. Москва", 228, 92, 89).need_dorm()
    is_olympiads = Technical("г. Москва", 228, 92, 89).has_olympiads()
    print(students_data)
