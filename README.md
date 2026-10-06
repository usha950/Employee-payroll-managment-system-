# Employee-payroll-management-system
An Employee Payroll Management System lets administrators add employee details and calculate salaries, including deductions. It generates payslips and saves payroll records for easy access and management.
# Employee Payroll Management System 
 
## About the Project 
 
Employee Payroll Management System is a simple Python project used to manage employee details and calculate employee salaries. 
 
The system allows users to add employees, view employee details, calculate salaries, generate payslips, and save payroll records. 
 
This project was created to practice Python programming concepts using a real-world payroll example. 
 
## Features 
 
- Add a new employee 
- Check for duplicate Employee IDs 
- View employee records 
- Calculate HRA and DA 
- Calculate Gross Salary 
- Calculate PF and Tax 
- Calculate Net Salary 
- Generate employee payslip 
- Save payroll records to a text file 
 
## Salary Calculation 
 
The project uses the following salary calculations: 
 
| Salary Component | Calculation | 
|---|---| 
| HRA | 20% of Basic Salary | 
| DA | 10% of Basic Salary | 
| Gross Salary | Basic Salary + HRA + DA | 
| PF | 12% of Gross Salary | 
| Tax | 5% of Gross Salary | 
| Net Salary | Gross Salary - Total Deduction | 
 
### Example 
 
For a Basic Salary of Rs. 10,000: 
 
- HRA = Rs. 2,000 
- DA = Rs. 1,000 
- Gross Salary = Rs. 13,000 
- PF = Rs. 1,560 
- Tax = Rs. 650 
- Total Deduction = Rs. 2,210 
- Net Salary = Rs. 10,790 
 
## Technologies Used 
 
- Python 
- Lists 
- Dictionaries 
- Functions 
- Loops 
- Conditional Statements 
- File Handling 
 
## Project Structure 
 
```text 
Employee-Payroll-Management/ 
| 
|-- main.py 
|-- employee.py 
|-- payroll.py 
|-- payslip.py 
|-- README.md
