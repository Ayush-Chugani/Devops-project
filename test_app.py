import pytest
from app import Employee, generate_report


def test_excellent_performance():
    emp = Employee(1, "Amit", "Present", 9)
    assert emp.calculate_performance() == "Excellent"


def test_good_performance():
    emp = Employee(2, "Neha", "Present", 6)
    assert emp.calculate_performance() == "Good"


def test_needs_improvement():
    emp = Employee(3, "Riya", "Absent", 3)
    assert emp.calculate_performance() == "Needs Improvement"


def test_negative_tasks():
    emp = Employee(4, "Karan", "Present", -1)
    with pytest.raises(ValueError):
        generate_report(emp)
