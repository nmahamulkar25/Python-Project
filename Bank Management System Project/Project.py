print("Create your bank Account")
aname=str(input("Enter Account holder name="))
ano=str(input("Enter account number of your choice="))
aamount=int(input("Enter amount to be kept in your account="))
i=str(input("Do you want to display your account details=(Yes/No)"))
def accdetails():
    print("Account Holder Details are as follows:")
    print("Account holder name=",aname)
    print("Account number=",ano)
    print("Account current balance=",aamount)
if(i=='Yes'):
    accdetails()
else:
    print("Thankyou")
o=str(input("Do you want to perform any operations on your account:(Yes/No)"))
if(o=='Yes'):
    print("Among the given option make a choice to perform operations= ")
    result=int(input("Enter 1 to deposit money into your bank account \n Enter 2 to withdraw money from your bank account"))
    if(result==1):
        a=int(input("Enter amount to be deposited into your account = "))
        aamount=a+aamount
        b=str(input("Do you want to display your account details:(yes/no)"))
        if(b=='yes'):
            accdetails()
    elif(result==2):
        n=int(input("Enter amount to withdraw from your bank account = "))
        aamount=aamount-b
        b=str(input("Do you want to display your account details:(yes/no)"))
    if(b=='yes'):
        accdetails()
    else:
        print("Enter valid operation choice to be performed")
else:
    print("Thankyou")
displaybankbalance=str(input("Do you want to Check or Display your Bank Balance:(Yes/No)"))
if(displaybankbalance=='Yes'):
    print("Account Current Balance = ",aamount)
else:
    print("Thankyou")
print("Thankyou for visiting our Bank")
    

    
    

