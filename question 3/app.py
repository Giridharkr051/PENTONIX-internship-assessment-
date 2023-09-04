from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (in-memory database)
departments = {
    10: 'Admin',
    20: 'Accounts',
    30: 'Sales',
    40: 'Marketing',
    50: 'Purchasing'
}

employees = [
    {"ENO": 1, "ENAME": "Amal", "DNO": 10, "SALARY": 30000},
    {"ENO": 2, "ENAME": "Shyamal", "DNO": 30, "SALARY": 50000},
    {"ENO": 3, "ENAME": "Kamal", "DNO": 40, "SALARY": 10000},
    {"ENO": 4, "ENAME": "Nirmal", "DNO": 50, "SALARY": 60000},
    {"ENO": 5, "ENAME": "Bimal", "DNO": 20, "SALARY": 40000},
    {"ENO": 6, "ENAME": "Parimal", "DNO": 10, "SALARY": 20000}
]

# API to return employee details by ENO
@app.route('/api', methods=['GET'])
def get_employee_by_ENO():
    try:
        ENO = int(request.args.get('ENO'))
        if not ENO:
            raise ValueError('ENO parameter is required')

        employee = next((emp for emp in employees if emp["ENO"] == ENO), None)
        if not employee:
            raise ValueError(f'Employee with ENO {ENO} not found')

        return jsonify(employee)
    except Exception as e:
        return jsonify(error=str(e)), 400

# API to return a list of employees by DNAME
@app.route('/api/employeesByDname', methods=['GET'])
def get_employees_by_DNAME():
    try:
        DNAME = request.args.get('DNAME')
        if not DNAME:
            raise ValueError('DNAME parameter is required')

        filtered_employees = [emp for emp in employees if departments.get(emp["DNO"]) == DNAME]
        if not filtered_employees:
            raise ValueError(f'No employees found in department with DNAME {DNAME}')

        return jsonify(filtered_employees)
    except Exception as e:
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(port=9000)
