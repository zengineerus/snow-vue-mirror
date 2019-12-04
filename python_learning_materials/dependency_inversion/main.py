from report_generator import ReportGenerator
from standard_output import StandardOutput
from employee_dao import EmployeeDao

if __name__ == '__main__':
    dao = EmployeeDao()
    output = StandardOutput()
    ReportGenerator(dao, output).print_employee_names()
