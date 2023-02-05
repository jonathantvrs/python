from datetime import date

class Employee:
    def __init__(self, name, birthdate, salary):
        self._name = name
        self._birthdate = birthdate
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    def age(self):
        splitted_birthdate = self._birthdate.split('/')
        birthyear = splitted_birthdate[-1]
        current_year = date.today().year
        return current_year - int(birthyear)

    def surname(self):
        name_without_whitespaces = self.name.strip()
        splitted_name = name_without_whitespaces.split()
        return splitted_name[-1]

    def calculate_bonus(self):
        value = self._salary * 0.1
        if value > 1000:
            raise Exception('Salary too high for bonus')
        return value

    def _is_partner(self):
        directors_surnames = ['Ptolomeu', 'Tavares', 'Nogueira', 'Silva']
        return (self._salary >= 100000 and (self.surname() in directors_surnames))

    def salary_decrease(self):
        if self._is_partner():
            self._salary -= self._salary * 0.1

    def __str__(self):
        return f'Employee({self._name}, {self._birthdate}, {self._salary})'