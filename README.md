# EXPENSE MANAGEMENT PROJECT
## OVERVIEW
This project is an object-oriented programming project in python. it is a simple expense manager that allows user manage financial expenses.
it has 2 classes, the Expense class and ExpenseDB class.
  * Expense – Represents an individual expense with attributes like title, amount, created_at, and updated_at.

  * ExpenseDB – Manages multiple Expense objects, providing methods to add, remove, and retrieve expenses.

Some of the key features are:
+ It creates and manages expenses with automatic timestamps.
+ It retrieves expenses by title or ID.
+ It stores expenses in an in-memory list.
+ It convert expenses to dictionaries for easy understanding.

### HOW TO CLONE THE REPOSITORY
Kindly run https://github.com/Becky090/altschool_exam_first_semester.git on your terminal locally. This will download the project to your local machine.
### TO RUN THE SCRIPT
Create a new Python file in the folder in Vs code or in any of your desired IDE. Import the classes from the file cloned and instantiate the classes.
Example:
```
from oop import Expense, ExpenseDB

expense_db = ExpenseDB()
expense1 = Expense("Books", 100.25)
expense_db.add_expense(expense1)
expense2 = Expense("Transport", 200.00)
expense_db.add_expense(expense2)

# Retrieve expenses by title
expenses = expense_db.get_expense_by_title("Transport")
for exp in expenses:
    print(exp.to_dict())

# Print all expenses
to_dict()
```
Thank you for your time.
