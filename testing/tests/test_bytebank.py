import pytest
from testing.code.bytebank import Employee

class TestClass:
    def test_when_age_gets_13_03_2000_returns_23(self):
        employee = Employee('test name', '13/03/2000', 4000)

        result = employee.age()

        assert result == 23

    def test_when_surname_gets_Jonathan_Tavares_returns_Tavares(self):
        employee = Employee('Jonathan Tavares', '13/03/2000', 4000)

        result = employee.surname()

        assert result == 'Tavares' 

    def test_when_salary_decrease_gets_100000_returns_90000(self):
        employee = Employee('Rebs Nogueira', '13/03/2000', 100000)

        employee.salary_decrease()

        assert employee.salary == 90000

    def test_when_calculate_bonus_gets_1000_returns_100(self):
        employee = Employee('Ana', '13/03/2000', 1000)

        result = employee.calculate_bonus()

        assert result == 100

    def test_when_calculate_bonus_gets_100000_returns_exception(self):
        with pytest.raises(Exception):
            employee = Employee('Ana', '13/03/2000', 100000)

            result == employee.calculate_bonus()

            assert result
