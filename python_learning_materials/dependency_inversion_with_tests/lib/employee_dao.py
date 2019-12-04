import MySQLdb

class EmployeeDao():
    def get_employees(self):
        db = MySQLdb.connect(user='root', host='127.0.0.1', db='py_employees')
        cursor = db.cursor()

        cursor.execute("""
            SELECT id, first, last FROM employees
            """)

        results = []

        row = cursor.fetchone()
        while row is not None:
            results += [row]
            row = cursor.fetchone()

        db.close()

        return results
