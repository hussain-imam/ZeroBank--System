from person import Person
class Account(Person):
    def __init__(self,name,age,cnic,balance):
        super().__init__(name,age,cnic)
        self.__balance=float(balance)
    def deposit(self,amount):
        if amount > 0:
            self.__balance=self.__balance + amount
            return True
        return False
    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance=self.__balance - amount
            return True
        return False
    def get_balance(self):
        return self.__balance
    def __str__(self):
        data=super().__str__()
        return f" Name: {self.name} | Balance: {self.__balance}".strip()
    def to_dict(self):
        data=super().to_dict()
        data['balance']=self.__balance
        return data
    @staticmethod
    def from_dict(data):
        return Account(data['name'], data['age'], data['CNIC'], data['balance'])
     
        


