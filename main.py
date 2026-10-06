from employee import add_employee, view_employees, employees
from payroll import calculate_salary
from payslip import generate_payslip


def save_records():
    with open("employee_records.txt", "w") as file:
        for employee in employees:
            salary = calculate_salary(employee["basic"])

            file.write("Employee ID: " + employee["id"] + "\n")
            file.write("Name: " + employee["name"] + "\n")
            file.write("Basic Salary: " + str(salary["basic"]) + "\n")
            file.write("Gross Salary: " + str(salary["gross"]) + "\n")
            file.write("Total Deduction: " + str(salary["deduction"]) + "\n")
            file.write("Net Salary: " + str(salary["net"]) + "\n")
            file.write("-----------------------------\n")

    print("\nRecords saved successfully!")


while True:
    print("\n==============================")
    print(" EMPLOYEE PAYROLL MANAGEMENT")
    print("==============================")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Generate Payslip")
    print("4. Save Records")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        emp_id = input("Enter Employee ID: ")
        found = False

        for employee in employees:
            if employee["id"] == emp_id:
                salary = calculate_salary(employee["basic"])
                generate_payslip(employee, salary)
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == "4":
        save_records()

    else:
        print("\nInvalid choice. Please try again.")
