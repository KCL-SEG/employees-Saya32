"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary=0, contract=0, commission=0, bonus=0, hourly_rate=0, hours=0):
        self.name = name
        self.salary = salary
        self.contract = contract
        self.commission = commission
        self.bonus = bonus
        self.hourly_rate = hourly_rate
        self.hours = hours


    def get_pay(self):
         return self.salary + (self.contract * self.commission) + self.bonus + (self.hours * self.hourly_rate)
        

    def __str__(self):
        return self.name + ' works on a ' + ('monthly salary' if self.contract == 0 else 'contract of ' + str(self.contract) + ' hours at ' + str(self.salary) + '/hour') + (' and receives a commission for ' + str(self.contract) + ' contract(s) at ' + str(self.commission) + '/contract' if self.commission != 0 else '') + (' and receives a bonus commission of ' + str(self.bonus) if self.bonus != 0 else '') + '. Their total pay is ' + str(self.pay) + '.'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary= 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', contract=100, salary=25, hours=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',  salary=3000, contract=4, commission=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',  contract=150, salary=25, commission=220, hours=150  )

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',salary=2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', contract=120, salary=30, bonus=600, hours=120)
