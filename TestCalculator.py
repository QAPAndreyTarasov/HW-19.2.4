import pytest

from app.Calculator import Calculator

class TestCalculator:
    def setup(self):
        self.Calculator = Calculator


    def test_multiply(self):
        assert self.Calculator.multiply(self, 5, 5) == 25

    def test_division(self):
        assert self.Calculator.division(self, 40, 8) == 5

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.Calculator.division(self, 40, 0)

    def test_subtraction_success(self):
        assert self.Calculator.subtraction(self, 15, 5) == 10

    def test_adding_success(self):
        assert self.Calculator.adding(self, 13, 7) == 20

    def teardown(self):
        print('Выполнение метода Teardown')