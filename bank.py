import os
import json
from account import Account
class Bank:
    def __init__(self,my_bank='ZeroBank', filename='accounts.json'):
        self.my_bank=my_bank
        self.filename=filename
        self.accounts={}
        self.load_from_file()
    def save_to_file(self):
        data={}
        for cnic,acc in self.accounts.items():
            data[cnic]=acc.to_dict()
            with open(self.filename,'w') as f:
                json.dump(data, f, indent=4)
    def load_from_file(self):
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename,'r') as f:
                 data =json.load(f)
                 for cnic,acc_data in data.items():
                     self.accounts[cnic]=Account.from_dict(acc_data)
        except:
            self.accounts={}
    def add_account(self,name,age,cnic,balance):
        if cnic in self.accounts:
            print(f"CNIC:{cnic} Account Exists in Branch")
            return False
        new_acc=Account(name,age,cnic,balance)
        self.accounts[cnic]=new_acc
        self.save_to_file()
        print(f" New Account Added: {self.my_bank}")
    def show_all_accounts(self):
        print(f'--- {self.my_bank}: All Acconts Detail ---')
        if not self.accounts:
            print('No Account Found')
            return 
        for acc in self.accounts.values():
            print(acc)
    def search_account(self,cnic):
        if cnic in self.accounts:
            print('Account Found')
            print(self.accounts[cnic])
            return self.accounts[cnic]
        else:
            print('Account Not Found')
            return None
    def deposit(self,cnic,amount):
        acc=self.search_account(cnic)
        if acc:
            acc.deposit(amount)
            self.save_to_file()
        else:
            print(f"Please Enter the Correct CNIC")    
    def withdraw(self,cnic,amount):
        acc=self.search_account(cnic)
        if acc:
            acc.withdraw(amount)
            self.save_to_file()
        else:
            print(f"CNIC Not Found")    
    def delete_account(self,cnic):
        if cnic in self.accounts:
            del self.accounts[cnic]
            self.save_to_file()
            print(f"Account {cnic} Deleted Successfully")
            return True
        else:
            print(f'Account With {cnic} not Found')
            return False
    def update_account(self,cnic,new_name,new_age):
        if cnic in self.accounts:
            self.accounts[cnic].name=new_name
            self.accounts[cnic].age=new_age
            self.save_to_file()
            print(f"Account with {cnic} updated Successfully")
            return True
        else:
            print('Account Not Found')
            return False
    def show_total_bank_value(self):
        total_accounts=len(self.accounts)    
        total_balance=sum(acc.get_balance() for acc in self.accounts.values())
        print(f'\n---- {self.my_bank} Branch Detail')
        print(f"Total Accounts: {total_accounts}")
        print(f"Total Value Of Branch: {total_balance}")




            


