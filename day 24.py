class PersonAccount:
    def __init__(self, firstname, lastname, age, income, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.income = income
        self.city = city
        self.incomes = set()
        self.expenses = set()

    def add_income(self, amount, description):
        self.incomes.add((amount, description))

    def add_expense(self, amount, description):
        self.expenses.add((amount, description))

    def total_income(self):
        return sum(amount for amount, desc in self.incomes)

    def total_expense(self):
        return sum(amount for amount, desc in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        print(f"Name: {self.firstname} {self.lastname}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")

PA = PersonAccount('Booby', 'Jhon', 20, 30000, 'skibidibump')

PA.add_income(5000, 'salary')
PA.add_income(200, 'bonus')
PA.add_expense(1500, 'rent')
PA.add_expense(300, 'food')

print(f"my firstname is: {PA.firstname}")
print(PA.lastname)
print(PA.age)
print(PA.income)
print(PA.city)

PA.account_info()