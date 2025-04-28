from numpy.f2py.capi_maps import depargs


class Employee:
    def __init__(self, name, age, rank, department, base_salary, bonus_eligible, working_hours = (8,17)):
        self.name = name
        self.age = age
        self.rank = rank
        self.department = department
        self.base_salary = base_salary
        self.bonus_eligible = bonus_eligible
        self.working_hours  = working_hours

    def get_info(self):
        return dict(
            name=self.name,
            age=self.age,
            rank=self.rank,
            department=self.department,
            base_salary=self.base_salary,
            bonus_eligible=self.bonus_eligible,
            working_hours={'start': self.working_hours[0], 'finish': self.working_hours[1]}
        )

    def __str__(self):
        info = self.get_info()
        return f"Name: {info.get('name', None)}, Age: {info.get('age', None)}, Rank: {info.get('rank', None)}, " \
               f"Department: {info.get('department', None)}, Base Salary: {info.get('base_salary', None)}, " \
               f"Bonus Eligible: {info.get('bonus_eligible', None)}, "\
               f"Working Hours: {info.get('working_hours', None).get('start', None)}-{info.get('working_hours', None).get('finish', None)}"

class Manager(Employee):
    def __init__(self, name, age, rank, department, base_salary, bonus_eligible, working_hours=(9,18), subs=None):
        super().__init__(name, age, rank, department, base_salary, bonus_eligible, working_hours)
        self.subordinates = subs


class Worker(Employee):
    def __init__(self, name, age, rank, department, base_salary, bonus_eligible, working_hours=(8,17), managed_by=None):
        super().__init__(name, age, rank, department, base_salary, bonus_eligible, working_hours)
        self.managed_by = managed_by

e = Manager('John', 32, 'worker','sales',10000, False)
print(e)