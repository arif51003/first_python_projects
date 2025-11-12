import uuid
from datetime import datetime,timezone
from Tranzaksiya import  Transaction

class BankAccount:
    def __init__(self,
                 id:uuid.UUID,
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
        
    def depos(self):
        status=False
        global accounts
        acc=None
        if not accounts:
            return "Akaunt mavjud emas"
        kart_num=input("Karta raqam kiriting:")
        for account in accounts:
            if kart_num==account.account_num:
                acc=account
                break
        if not acc:
            print("Akkaunt mavjud emas")
            return
        try:
            qiymat=int(input("O'tkazma summasi:"))
            if qiymat<=0:
                print("Summa 0 dan katta bo'lishi kerak")
                return
        except:
            print("Faqat raqam kiriting")
            return
        acc.balance+=qiymat
        status=True
        
        new_tranzak=Transaction(
            id=uuid.uuid4(),
            type="Depozit",
            sender_nm="Unknown",
            receiver_nm=acc.name,
            amount=qiymat,
            status=status,
            datetime=datetime.now(timezone.utc)
        )
        acc.transactions.append(new_tranzak)
            
    
    def whithdrav(self):
        status=False
        global accounts
        acc=None
        if not accounts:
            return "Akaunt mavjud emas"
        kart_num=input("Karta raqam kiriting:")
        for account in accounts:
            if kart_num==account.account_num:
                acc=account
                break
        if not acc:
            print("Akkaunt mavjud emas")
            return
        try:
            qiymat=int(input("O'tkazma summasi:"))
            if qiymat<=0:
                print("Summa 0 dan katta bo'lishi kerak")
                return
        except:
            print("Faqat raqam kiriting")
            return
        acc.balance-=qiymat
        status=True
        new_tranzak=Transaction(
            id=uuid.uuid4(),
            type="Whitdraw",
            sender_nm=acc.name,
            receiver_nm="Unknown",
            amount=qiymat,
            status=status,
            datetime=datetime.now(timezone.utc)
        )
        acc.transactions.append(new_tranzak)
        
    def __str__(self):
        return f"BankAccount:<name:{self.name}>"



accounts:list[BankAccount]=[]

current_account= None

def creat_account():
    print("Malumotlarni to'ldiring")
    
    name = input("F.I.Sh: ")
    account_num = input("Akkount raqam: ")
    balance = int(input("Mavjud balans: "))
    id : uuid.UUID = uuid.uuid4()
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
        print(f"{i+1}.{account.name}-{account.balance}---{str(account.created_at)[:19]} da yaratilgan")
    end :str = input("Yakunlash 'Enter'")
    if end=='\n':
        return None
    
    

def search_acc():
    n=input("Search:")
    print("=====Natijalar=====")
    for account in enumerate(accounts):
        if n.lower() in account.name.lower():
            print(f'id:{str(account.id)}-{account.name}')


