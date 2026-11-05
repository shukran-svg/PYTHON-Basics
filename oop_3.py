#classes
# customer -names ,email, kra ,dob ,gender
#BankAccount -customer ,acc_no ,acc_type ,balance
class Customer:
    def __init__(self,names:str,email:str ,kra:str,dob:str,gender:str):
        self.names =names
        self.email =email
        self .kra =kra
        self .dob =dob
        self .gender =gender
    def show_details(self):
        print(f"Name : {self.names} and KRA PIN: {self.kra}")
        # return f"Name : {self.names} and KRA PIN :{self.kra}"
class Account:
    def __init__(self,owner:Customer,acc_no:str,acc_type:str,balance:float ):
        self.owner = owner
        self.acc_no= acc_no
        self.acc_type= acc_type
        self.balance =balance
    def print_details(self):
        print(self.owner.names)
        print(self.acc_no)
        print(self.balance)
        print("***********")
    def deposit(self,amount:float):
        self.balance += abs (amount)

    def withdraw (self,amount:float):
        if amount> self.balance:
            print("insufficient funds")
        else:
            self.balance -= abs(amount)

    def __str__(self):
        return f"Account No {self.acc_no}  for  {self.owner.names}"




owner1 = Customer("Susan Nathaniel","ss@gmail.com","KRA001","31-8-2004","F")
owner2 = Customer("Martin Micheal","mm@gmail.com","KRA002","1-8-2004","M")
owner3 = Customer("Mary Milly","mm@gmail.com","KRA004","11-8-2004","F")
owner4 = Customer("John Doe","jd@gmail.com","KRA005","15-8-2004","M")
owner5 = Customer("Jane Smith","js@gmail.com","KRA006","20-8-2004","F")





acc1 =Account(owner1,"987643","current",90_000)
acc2 =Account(owner2,"677643","current",50_000)
acc3 =Account(owner3,"345643","current",70_000)
acc4 =Account(owner4,"456789","current",60_000)
acc5 =Account(owner5,"567890","current",80_000)

#print(owner1.show_details())
#print(owner1.dob) # private



acc1.print_details()
acc1.deposit(-9000)
acc1.print_details()
acc1.withdraw(1_000)
acc1.print_details()

print (acc1)





#acc2.print_details()
#acc2.deposit(-9009)
#acc2.withdraw(1000)


#acc3.print_details()
#acc3.deposit(-9009)
#acc3.withdraw(1000)

#acc4.print_details()
#acc4.deposit(-9009)
#acc4.withdraw(1000)

#acc5.print_details()
#acc5.deposit(-9009)
#acc5.withdraw(1000)






