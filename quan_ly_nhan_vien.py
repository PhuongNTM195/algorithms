class employee:
    def __init__(self, name, age, address, role, basic_salary, exp, working_hours):

        pass


    def get_bonus(self):

        pass


    def get_income(self):

        pass

    def __str__(self):
        return self.name + '; ' + str(self.age) + '; ' + self.address + '; ' + self.role + '; ' + str(self.exp) + '; ' + str(self.basic_salary) + '; ' + str(self.working_hours)

class employee_management:
    def __init__(self):
        self.employees = self.read_data("employee_input.txt")

    def print_infos(self):
        for i in range(len(self.employees)):
            print(self.employees[i])


    def read_data(self, file_name):

        pass


    def sort_by_income(self):

        pass


    def get_max_income(self, employee1):

        pass