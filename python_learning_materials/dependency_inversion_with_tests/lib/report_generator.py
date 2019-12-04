class ReportGenerator:

    def __init__(self, dao, output):
        self._dao = dao
        self._output = output
    
    def print_employee_names(self):
        try:
            employees = self._dao.get_employees()

            self._output.print_line('ID - Last, First')

            for employee in employees:
                line = "{0} - {2}, {1}".format(employee[0], employee[1], employee[2])

		self._output.print_line(line)
        except Exception:
            self._output.print_line("An error occurred...")
            raise

