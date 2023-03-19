from datetime import datetime
balance=0
l={}
srno=1
def deposit(money):
    global balance,srno
    balance+=int(money)
    tme = datetime.now().strftime("%d/%m%Y    %H:%M:%S")
    data="added  "+str(money)+" and "+str(tme)
    l.update({srno:data})
    srno+=1

def withdraw(money):
    global balance,srno
    if int(money)<=balance:
        balance-=int(money)
        tme=datetime.now().strftime("%d/%m%Y    %H:%M:%S")
        data="withdrawl "+str(money) +"and"+str(tme)
        l.update({srno:data})
        srno+=1
    else:
        print("not valid ")
        print("you have unsufficient balance")


if __name__=="__main__":
    while True:
        a=input("type here:")
        if "deposit" in a:
            try:
                li=a.split()
                deposit(li[1])
            except:
                a=input("enter the value:")
                try:
                    a=int(a)
                    deposit(a)
                except:
                    print("invalid statement")
        elif "checkbal" in a:
            print(balance)
        elif "clearbal" in a:
            balance=0
        elif "mypas" in a:
            for i in l.keys():

                a=l[i]
                myli=a.split("and")
                print(myli[1])
                print(myli[0])
        elif "withdraw" in a:
            try:
                li=a.split(" ")
                withdraw(li[1])
            except:
                a=input("enter the value")
                try:
                    a=int(a)
                    withdraw(a)
                except:
                    print('invalid statement')
        elif "all" in a:
            print("withraw: for withdrawing money")
            print("deposit: for depositing money")
            print("clearbal: for clearing balance")
            print("checkbal: for checking balance")





