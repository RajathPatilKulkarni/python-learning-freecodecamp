class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name

    def deposit(self, amount, description = ''):
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount,
                'description': description
            })
            return True
        return False

    def transfer(self, amount, category):
        if self.withdraw(amount, f'Transfer to {category.name}'):
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        output = self.name.center(30, '*') + '\n'
        for item in self.ledger:
            desc = item['description'][:23].ljust(23)
            amt = f'{item["amount"]:.2f}'.rjust(7)
            output += desc + amt + '\n'
        output += f'Total: {self.get_balance():.2f}'
        return output


def create_spend_chart(categories):
    withdrawals = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total += -item['amount']
        withdrawals.append(total)

    total_spend = sum(withdrawals)
    percentages = [(int ((w / total_spend) * 100) // 10) * 10 for w in withdrawals]

    chart = 'Percentage spent by category\n'
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + '| '
        for p in percentages:
            chart += 'o  ' if p >= i else '   '
        chart += '\n'

    chart += '    ' + '-' * (len(categories) * 3 + 1) + '\n'

    max_len = max(len(c.name) for c in categories)
    for i in range(max_len):
        chart += '     ' 
        for c in categories:
            chart += (c.name[i] if i < len(c.name) else ' ') + '  '
        chart += '\n'

    return chart.rstrip('\n')
