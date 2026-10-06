@@ -4,11 +4,8 @@


def save_records():

    with open("employee_records.txt", "w") as file:

        for employee in employees:

            salary = calculate_salary(employee["basic"])

            file.write("Employee ID: " + employee["id"] + "\n")
@@ -23,16 +20,13 @@ def save_records():


while True:

    print("\n==============================")
    print(" EMPLOYEE PAYROLL MANAGEMENT")
    print("==============================")

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Generate Payslip")
    print("4. Save Records")
    print("5. Exit")

    choice = input("Enter your choice: ")

@@ -43,19 +37,13 @@ def save_records():
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

@@ -65,10 +53,5 @@ def save_records():
    elif choice == "4":
        save_records()

    elif choice == "5":

        print("\nThank you for using Employee Payroll Management System!")
        break

    else:
        print("\nInvalid choice. Please try again.")
        print("\nInvalid choice. Please try again.")
