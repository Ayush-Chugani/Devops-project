class Employee:
    def __init__(self, emp_id, name, attendance, tasks_completed):
        self.emp_id = emp_id
        self.name = name
        self.attendance = attendance
        self.tasks_completed = tasks_completed

    def calculate_performance(self):
        if self.tasks_completed >= 8:
            return "Excellent"
        elif self.tasks_completed >= 5:
            return "Good"
        else:
            return "Needs Improvement"


def generate_report(employee):
    if employee.tasks_completed < 0:
        raise ValueError("Tasks completed cannot be negative")

    report = {
        "ID": employee.emp_id,
        "Name": employee.name,
        "Attendance": employee.attendance,
        "Tasks Completed": employee.tasks_completed,
        "Performance": employee.calculate_performance()
    }
    return report


if __name__ == "__main__":
    emp = Employee(101, "Rahul", "Present", 6)
    report = generate_report(emp)

    print("Employee Performance Report")
    print("---------------------------")
    for key, value in report.items():
        print(f"{key}: {value}")
