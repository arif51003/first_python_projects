# Final Project - Bank Account Management System

Mazkur project Python moduli uchun yakuniy CLI dastur bo'lib, ushbu modulda o'tilgan barcha mavzularni qamrab oladi. Projectning maqsadi Bank operatsiyalari bajarilishini simulyatsiya qilish va shu o'rinda OOP, funksiyalar, fayllar bilan ishlash va boshqa ko'plab Python featurelarini amalda qo'llashdan iborat.

---

### Overview

Main Menu quyidagi ko'rinishda bo'ladi:

```
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
```

Dasturni 3 bosqichli tuzib boramiz. Quyida har bir bosqichda aynan qanday tasklar bajarilishi bilan tanishasiz.

#### Version 1: Core Logic (non-persistent storage)

Dastlabki bosqichda biz barcha fundamental birliklar va strukturalarni qurib olamiz. Ma'lumotlar persistent emas, ya'ni dasturni to'xtatib boshidan ishga tushirganda ma'lumotlar yo'qoladi. 

Tuzishimiz kerak bo'lgan konstruksiyalar:
- `BankAccount` classi. 
    - Atributlari: id: uuid, name: str, account_number: str (5440 8100 1234 4321 kabi), balance: int, transactions: list[Transaction]
    - Metodlari: deposit(amount: int), withdraw(amount: int), display_info(), record_transaction(type: str, amount: int)
- `Transaction` classi.
    - Atributlari: id: uuid, type: str, sender_name: str, receiver_name: str, amount: int, status: str, datetime: datetime
    - Metodlari: `__str__()


Barcha accountlar `accounts` deb nomlangan listda saqlanadi. Bunda, list ichida `BankAccount` klassidan olingan “mahsulot”lar, yoxud obyektlar saqlanadi. Masalan:

```python
class BankAccount:
	# O'ziz yozasiz
	pass

account1 = BankAccount()
accounts.append(account1)
```

Tranzaksiyalar esa har bir `BankAccount` classining `transactions` listida saqlanadi.

Quyida bizga kerak bo'lgan funksiyalar bilan tanishamiz:

**1. Create New Account**
- Foydalanuvchidan ism, akkaunt raqami va dastlabki summani so'rang.
- id fieldi uchun `uuid()` kutubxonasidan foydalanib unique ID yarating.
- yaratilgan `BankAccount` obyektini `accounts` listiga qo'shing.

**2. View All Accounts**
Tizimda mavjud barcha akkauntlarni list qilib chiqaradi. Bunda BankAccount objectining `display_info()` yoki `__str__()` methodidan foydalaning.

**3. Search Account**
List ichidan kiritilgani bo’yicha account qidirish. Bunda user account nomi bo’yicha qidirishi mumkin.

**4. Deposit**
Accountga pul kirimi. `balance` atributini to’g’ridan-to’g’ri emas, maxsus method bilan (masalan `deposit()`) o’zgartirasiz. Amalga oshirilgan transaksiyalar transactions listiga saqlab boriladi. Har bir transaksiya alohida dictionary sifatida saqlanishi kerak, bunda uning tuzilishi:

```python
transaction = {
	"datetime": "2025-13-04 13:00:00.000Z", # or datetime object
	"account_holder": "account_holder_name",
	"account_number": "account_number",
	"amount": 500,
	# other related data if any
}
```

**5. Withdraw**
Accountdan pul chiqimi. Bunda ham balance attributini shu method yordamida kamaytirasiz (belgilangan miqdorda). Amalga oshirilgan transaksiya transactions listiga dictionary ko’rinishida saqlanadi.

**6. View Transactions**
Mazkur akkauntda amalga oshirilgan transaksiyalar listini ko’rish. Bunda transactions listi (atribut) bo’ylab iterate qilinadi va har bir transaction dictionarysi ichidagi ma’lumot ekranga chiqariladi.

**7. Delete Account**
Accountni o’chirish imkoniyati. Agar user akkauntini o’chirishga qaror qilsa, shu user account raqami bilan bir xil fayl ochiladi va barcha tranzaksiyalari faylga saqlab qo’yiladi.

**8. Exit**
Chiqish.

---

#### Version 2: Adding Persistent Storage (File and JSON)
