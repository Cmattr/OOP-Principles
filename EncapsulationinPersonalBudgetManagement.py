#Task 1: Define Budget Category Class
class BudgetCategory:
    def __init__(self, category_name, allocate_budget):
        self._category_name = category_name
        self._allocate_budget = allocate_budget
        self._budget = 0
    #Task 2: Implement Getters and Setters
    # get statements
    def get_category_name(self):
        return self._category_name

    def get_allocate_budget(self):
        return self._allocate_budget

    def get_budget(self):
        return self._budget
    #set statements
    def set_category_name(self, new_category):
        self._category_name = new_category

    def set_allocate_budget(self, new_budget):
        self._allocate_budget = new_budget

    def set_budget(self, new_amount):
        self._budget = new_amount
   
    #Task 3: Add Budget Functionality
    # set the amount of the budget
    def budget_amount(self, amount):
        if amount > 0:
            self.set_budget(self.get_budget() + amount)
            print(f"New amount for budgeting: ${amount}")
        else:
            print("The amount for budgeting must be above $0.00")
    #add new budget expenses
    def add_expense(self, expense_name, value):
        if 0 < value < self.get_budget():
            self._budget -= value
            print(f"New item {expense_name} has been budgeted for the amount of ${value}")
        else:
            print("Something has gone wrong, please try again")
    
    #Task 4: Display Budget Details
    def display_details(self):
        print(f"Category Name: {self.get_category_name()}")
        print(f"Allocated Budget: ${self.get_allocate_budget()}")
        print(f"Remaining Budget: ${self.get_budget()}")


expense = BudgetCategory("food", 50)
expense.budget_amount(500)
expense.add_expense("groceries", 100)
expense.display_details()