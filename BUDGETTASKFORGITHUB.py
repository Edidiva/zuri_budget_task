class Budget():
    def __init__(self, name):
        self.name = name
        self.balance = 0
   
    def deposit(self, amount):
        self.balance = amount 

        return f"your new balance is {self.balance} in {self.name} budget" 
    
    def withdraw(self, amount):
        if self.balance < amount:
            return "insufficient funds"
        else:
            self.balance = self.balance - amount

            feedback = 'transaction successful\n'
            feedback += f'your new balance is {self.balance} in {self.name} budget'

            return feedback
    def get_balance(self):
        return f"your balance is {self.balance}"

    def transfer(self, amount, category):
        if self.name == category.name:
            feedback = "Oops an error ocuured, you can't transfer into the same category" 
            return feedback
        elif self.balance < amount:
            feedback = "insufficient balance"
            return feedback
        else:
            self.balance -= amount
            category.balance += amount 
            feedback = 'transfer was succeful\n'
            feedback += f'your new balance for {self.name} is {self.balance}\n'
            feedback += f'your new balance for {category.name} is {category.balance}\n'

            return feedback

     


food = Budget("food")
clothing = Budget("clothing") 
entertainment = Budget("entertainment")

