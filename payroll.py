def calculate_salary(basic_salary):

    hra = basic_salary * 0.20
    da = basic_salary * 0.10

    gross_salary = basic_salary + hra + da

    pf = gross_salary * 0.12
    tax = gross_salary * 0.05

    total_deduction = pf + tax

    net_salary = gross_salary - total_deduction

    salary_details = {
        "basic": basic_salary,
        "hra": hra,
        "da": da,
        "gross": gross_salary,
        "pf": pf,
        "tax": tax,
        "deduction": total_deduction,
        "net": net_salary
    }

    return salary_details
