import uuid
import datetime
from datetime import timezone,datetime

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
