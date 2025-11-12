from Bank_acc import *

menutxt='''
=== Bank System Menu ===
1. Create New Account
2. View All Accounts
3. Search Account
4. Deposit
5. Withdraw
6. View Transactions
7. Delete Account
8. Exit
========================
'''
def main_menu():
    
    while True:
        print(menutxt)
        
        choice=int(input("Tanlov:"))

        if choice==1:
            global current_account
            
            current_account = creat_account()
            print("Successfully")

        elif choice == 2:
            
            view_all_acc()

        elif choice == 3:
            search_acc()
        elif choice == 4:
            BankAccount.depos()
        elif choice == 5:
            print("Withdraw")
        elif choice == 6:
            print("View Transactions")
        elif choice == 7:
            print("Delete Account")
        else:
            print('Exit')
            break
        

if __name__=="__main__":
    main_menu()
        
    