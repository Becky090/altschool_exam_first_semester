import uuid
from datetime import datetime, timezone


class Expense:
    def __init__(self, title: str, amount: float):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at

    def update(self, title: str = None, amount: float = None):
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }


class ExpenseDB:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)

    def remove_expense(self, expense_id: str):
        self.expenses = [pense for pense in self.expenses if pense.id != expense_id]

    def get_expense_by_id(self, expense_id: str):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expense_by_title(self, title: str):
        return [exp for exp in self.expenses if exp.title.lower() == title.lower()]

    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]
