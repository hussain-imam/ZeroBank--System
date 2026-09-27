from bank import Bank
my_bank=Bank(my_bank='ZeroBank')
while True:
    print('\n --- ZeroBank Main Menu ---')
    print('1- New Opening Account Form ')
    print('2- Cash Deposit')
    print('3- Cash Withdraw')
    print('4- Account Searching with CNIC')
    print('5- Show All Accounts')
    print('6- Account Delete Option')
    print('7- Acoount Update Option')
    print('8- Bank Total Account Values')
    print('9- Exit')

    choice= input('Please Enter Your Option: ').strip()
    if choice == '1':
        name=input('Please Enter the Name')
        age=input('Please Enter the Age')
        cnic=input('Please Enter the CNIC')
        balance=float(input('Please Enter the Amount'))
        my_bank.add_account(name,age,cnic,balance)
    elif choice == '2':
        cnic=input('Please Enter the CNIC')
        amount=float(input('Please Enter the Amount'))
        my_bank.deposit(cnic,amount) 
    elif choice == '3':
        cnic=input('Please Enter the CNIC')
        amount=float(input('Please Enter the Amount'))
        my_bank.withdraw(cnic,amount)
    elif choice == '4':
        cnic=input('Please Enter the CNIC')
        my_bank.search_account(cnic)
    elif choice == '5':
        my_bank.show_all_accounts()
    elif choice == '6':
        cnic= input('Please Enter the CNIC for Deletion')
        my_bank.delete_account(cnic)
    elif choice == '7':
        cnic=input('Please Enter the CNIC for Updating ')
        new_name=input("Please Enter the New Name")
        new_age=int(input('Please Enter the New Age'))
        my_bank.update_account(cnic,new_name,new_age)
    elif choice == '8':
        my_bank.show_total_bank_value()
    elif choice == '9':
        print('Bank Closed')
        break
    else:
        print('Thank You Using ZeroBank')
                        
