

f = open("password.txt")
userpassword = f.read()
f.close()
b = open("balance.txt")
balance = b.read()
nb=int(balance)
b.close()


def mainatm():
    
        n=2
        for i in range(3):
           
            a = (input("enter the  four number password: "))
            if a == userpassword:
                option()        
                break
            elif i == 3:
                print("blocked")
            else:
                c=n-i
                print("wrong password try again")
                print ("{} attempt remaining".format(c))

           
def withdrawl():
    print('''
             1 current
             2 saving''')
    a = int(input("current or saving: "))
    if a == 1:
        c = int(input("enter the money you want to withdrawl your current account: "))
        if c <= nb:
            with open("balance.txt") as f:
                balance = f.read()
                t = int(balance)
                abalance = t-c
                nbalance = str(abalance)

            with open("balance.txt", "w") as f:
                f.write(nbalance)

            print("withdrawl sucesfull")

        else:
            print("out of money")

    elif a == 2:
        s = int(input("enter the money you want to withdrawl your saving account: "))
        if s <= nb:
            with open("balance.txt") as f:
                balance = f.read()

                t = int(balance)

                abalance = t-s

                nbalance = str(abalance)

            with open("balance.txt", "w") as f:
                f.write(nbalance)

            print("withdrawl sucesfull")

        else:
            print("out of money")

    else:
        print("choice not available enter a right choice")


def chanpass():
    
        n = input("enter a new four digit password: ")
        with open("password.txt", "w") as f:
            f.write(n)
            
        
        
        

        print("your new password updated succesfully")
        
    

def option():
    options = '''welcome
           1. Withdrawl
           2. enquire
           3. change password
           4. exit'''

    print(options)
    choice()


def choice():

    while(True):
        a = int(input('Enter a choice: '))
        if a == 1:
            withdrawl()
        elif a == 2:
            b = open("balance.txt")
            balance = b.read()
            print(balance)
        elif a == 3:
            chanpass()
        elif a == 4:
            print('Thanks for coming')
            break
        else:
            print("choice not available, please  choose given choices")


mainatm()
