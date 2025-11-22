class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title_line = '*' * ((30 - len(self.name)) // 2) + self.name + '*' * ((30 - len(self.name) + 1) // 2)
        lines = [title_line[:30]]
        for item in self.ledger:
            desc = item['description'][:23].ljust(23)
            amt = f"{item['amount']:>7.2f}"
            lines.append(f"{desc}{amt}")
        lines.append(f"Total: {self.get_balance():.2f}")
        return '\n'.join(lines)


def create_spend_chart(categories):
    # Calculate spending percentages
    total_spent = sum(sum(-item['amount'] for item in cat.ledger if item['amount'] < 0) for cat in categories)
    percentages = []
    for cat in categories:
        spent = sum(-item['amount'] for item in cat.ledger if item['amount'] < 0)
        pct = (spent / total_spent * 100) if total_spent > 0 else 0
        percentages.append(int(pct // 10) * 10)  # Round down to nearest 10

    # Build the chart
    lines = ["Percentage spent by category"]

    # Percentage bars
    for p in range(100, -1, -10):
        line = f"{p:>3}| "
        for pct in percentages:
            line += "o  " if pct >= p else "   "
        lines.append(line)

    # Horizontal line - fixed to have 3 dashes per category + 1 extra at the end
    num_categories = len(categories)
    horizontal_line = "    -" + "---" * num_categories
    lines.append(horizontal_line)

    # Category names vertically
    max_len = max(len(cat.name) for cat in categories) if categories else 0
    for i in range(max_len):
        line = "     "
        for cat in categories:
            if i < len(cat.name):
                line += cat.name[i] + "  "
            else:
                line += "   "
        lines.append(line)

    return '\n'.join(lines)
