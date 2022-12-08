class Employee:
    def __init__(self, name, salary = 0, pay_rate = 0, contract_hours = 0, commission_contracts = 0, bonus_commission=0, commision_rate =0):
        self.name = name
        self.pay_rate = pay_rate
        self.salary = salary
        self.contract_hours = contract_hours
        self.commission_contracts = commission_contracts
        self.bonus_commission = bonus_commission
        self.commision_rate = commision_rate

    def get_pay(self):
        pay = 0
        if self.salary:
            pay += self.salary
        if self.contract_hours and self.pay_rate:
            pay += self.contract_hours * self.pay_rate
        if self.commission_contracts and self.commision_rate:
            pay += self.commission_contracts * self.commision_rate
        if self.bonus_commission:
            pay += self.bonus_commission
        return pay

    def __str__(self):
        s = f'^{self.name} works on '
        if self.salary:
            s += f'a monthly salary of {self.salary} '
        if self.contract_hours and self.pay_rate:
            s += f'a contract of {self.contract_hours} hours at {self.pay_rate}/hour '
        if self.commission_contracts and self.commision_rate:
            s += f'a commission for {self.commission_contracts} contract(s) at {self.commision_rate}/contract'
        if self.bonus_commission:
            s += f'and receives a bonus commission of {self.bonus_commission}.'
        s += f'\\s+Their total pay is {self.get_pay()}.$'
        return s

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', pay_rate=25, contract_hours=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', pay_rate=0, salary=3000, commission_contracts=4, commision_rate=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', pay_rate=25, contract_hours=150, commission_contracts=3, commision_rate= 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary=2000, bonus_commission=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', pay_rate=30, contract_hours=120, bonus_commission=600)
