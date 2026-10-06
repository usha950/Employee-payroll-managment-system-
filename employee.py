employees = []


def add_employee():
    print("\n--- Add Employee ---")

    emp_id = input("Enter Employee ID: ")

    # Check duplicate ID
    for employee in employees:
        if employee["id"] == emp_id:
            print("Employee ID already exists!")
            return

    name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))

    employee = {
        "id": emp_id,
        "name": name,
        "basic": basic_salary
    }

    employees.append(employee)

    print("Employee added successfully!")


def view_employees():
    print("\n--- Employee Records ---")

    if len(employees) == 0:
        print("No employee records found.")
        return

    for employee in employees:
        print("\nEmployee ID:", employee["id"])
        print("Name:", employee["name"])
        print("Basic Salary: ₹", employee["basic"])
