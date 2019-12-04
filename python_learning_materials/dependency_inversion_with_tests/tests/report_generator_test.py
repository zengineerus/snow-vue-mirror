import pytest
from lib.report_generator import ReportGenerator

class FakeDao:
    def __init__(self):
        self.data = []
        self.should_blow_up = False

    def get_employees(self):
        if self.should_blow_up:
            raise Exception('oh noes!')
        return self.data

class FakeOutput:
    def __init__(self):
        self.lines_printed = []

    def print_line(self, line):
        self.lines_printed += [line]

class TestReportGenerator():
    def setup_method(self, method):
        self.dao = FakeDao()
        self.output = FakeOutput()

        self.test_object = ReportGenerator(self.dao, self.output)

    def test_print_header_only_when_no_employees_present(self):
        self.test_object.print_employee_names()

        assert len(self.output.lines_printed) == 1
        assert self.output.lines_printed[0] == 'ID - Last, First'

    def test_print_a_row_for_each_employee(self):
        self.dao.data = [('', '', ''), ('', '', ''), ('', '', '')]

        self.test_object.print_employee_names()

        assert len(self.output.lines_printed) == 4

    def test_raise_exception_if_db_fails(self):
        self.dao.should_blow_up = True

        with pytest.raises(Exception) as e:
            self.test_object.print_employee_names()

    def test_log_error_if_db_fails(self):
        self.dao.should_blow_up = True

        with pytest.raises(Exception) as e:
            self.test_object.print_employee_names()

        assert self.output.lines_printed[-1] == 'An error occurred...'

