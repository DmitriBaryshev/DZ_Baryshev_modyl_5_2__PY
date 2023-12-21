import json


class EmployeeSystem:
    def __init__(self, filename):
        self.filename = filename
        self.employees = self.load_employees()

    def load_employees(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_employees(self):
        with open(self.filename, 'w') as file:
            json.dump(self.employees, file)

    def add_employee(self, employee_data):
        self.employees.append(employee_data)
        self.save_employees()

    def edit_employee(self, index, new_employee_data):
        self.employees[index] = new_employee_data
        self.save_employees()

    def delete_employee(self, index):
        del self.employees[index]
        self.save_employees()

    def find_employee_by_last_name(self, last_name):
        return [employee for employee in self.employees if employee['last_name'] == last_name]

    def find_employee_by_age(self, age):
        return [employee for employee in self.employees if employee['age'] == age]

    def find_employee_by_initial(self, initial):
        return [employee for employee in self.employees if employee['last_name'].startswith(initial)]

    def print_all_employees(self):
        for employee in self.employees:
            print(employee)


# Пример использования
filename = "employees.json"
system = EmployeeSystem(filename)

# Добавление сотрудников
system.add_employee({'first_name': 'Иван', 'last_name': 'Иванов', 'age': 30})
system.add_employee({'first_name': 'Петр', 'last_name': 'Петров', 'age': 25})

# Редактирование сотрудника
system.edit_employee(0, {'first_name': 'Новое имя', 'last_name': 'Новая фамилия', 'age': 40})

# Удаление сотрудника
system.delete_employee(1)

# Поиск сотрудников
print(system.find_employee_by_last_name('Иванов'))
print(system.find_employee_by_age(40))
print(system.find_employee_by_initial('Н'))

# Вывод информации обо всех сотрудниках
system.print_all_employees()
