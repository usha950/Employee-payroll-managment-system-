def generate_payslip(employee, salary):

    print("\n==============================")
    print("        EMPLOYEE PAYSLIP")
    print("==============================")

    print("Employee ID :", employee["id"])
    print("Name        :", employee["name"])

    print("------------------------------")

    print(f"Basic Salary: ₹{salary['basic']:.2f}")
    print(f"HRA         : ₹{salary['hra']:.2f}")
    print(f"DA          : ₹{salary['da']:.2f}")
    print(f"Gross Salary: ₹{salary['gross']:.2f}")

    print("------------------------------")

    print(f"PF Deduction: ₹{salary['pf']:.2f}")
    print(f"Tax         : ₹{salary['tax']:.2f}")
    print(f"Total Ded.  : ₹{salary['deduction']:.2f}")

    print("------------------------------")

    print(f"NET SALARY  : ₹{salary['net']:.2f}")

    print("==============================")
