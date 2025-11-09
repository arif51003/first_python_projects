import  datetime
import uuid
from datetime import timezone

class Transaction:
    def __init__(self,
                 id:uuid,
                 type:str,
                 sender_nm:str,
                 receiver_nm:str,
                 amount:int,
                 status:str,
                 datetime:datetime):
        self.id=id
        self.type=type
        self.sender_nm=sender_nm
        self.receiver=receiver_nm
        self.amount=amount
        self.status=status
        self.datetime=datetime
        
    def __str__(self):
        return f"Transaction:<id={str({self.id})}>"
    
class BankAccount:
    def __init__(self,
                 id:uuid,
                 name:str,
                 account_num:int,
                 balance:int,
                 created_at:datetime):
        self.id=id
        self.name=name
        self.account_num=account_num
        self.balance=balance
        self.created_at=created_at
        self.transactions:list[Transaction] = []
        
        
    def __str__(self):
        return f"BankAccount:<name:{self.name}>"



accounts:list[BankAccount]=[]

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
Enter your choice: 
'''

current_account= None

def creat_account():
    print("Malumotlarni to'ldiring")
    
    name = input("F.I.Sh")
    account_num = input("Akkount raqam:")
    balance = int(input("Mavjud balans:"))
    
    id : uuid.UUID = uuid.uuid4
    creat_at = datetime.now(timezone.utc)
    
    new_account=BankAccount(
        id=id,
        name=name,
        account_num=account_num,
        balance=balance,
        created_at=creat_at
    )
    global accounts
    accounts.append(new_account)
    
    return new_account

def view_all_acc():
    print("Barcha akkount:")
    for i, account in enumerate(accounts):
        return f"{i+1}.{account.name}-{account.balance}"
    
    

def search_acc():
    pass

def depos():
    pass

def whithdr():
    pass

def view_all_tranzak():
    pass

def del_acc():
    pass 
  
  
def main_menu():
    print(menutxt)
    
    while True:
        
        choice=int(input("Tanlov:"))

        if choice==1:
            global current_account
            
            current_account = creat_account()
            print("Successfully")

        elif choice == 2:
            
            print("View All Accounts:")
            for account in accounts:
                print(account)

        elif choice == 3:
            
            print("Search Account")
        elif choice == 4:
            print("Deposit")
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
        
    