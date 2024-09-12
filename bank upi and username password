un_amt={'dinga':1000,'manga':1200}
un_pass={'dinga':123,'mamga':456}
un_upi={'dinga':2508,'manga':1490}

username=input("enter user name:")
password=int(input("enter the password:"))
balance=0

def deposite():
     balance=un_amt[username]+amt
     print(f'your bank balance is {un_amt[username]} ')
     un_amt[username]=balance

     print( f'deposited amount is {amt} and total amount is {balance}')


def withdraw():
    wbalance=un_amt[username]-withdraw_amt
    print(f'your bank balance is {un_amt[username]}')
    un_amt[username]=wbalance

    print(f'and withdrawal amount is {withdraw_amt} and your final balance is {wbalance}')


def balance_check():
    total_balance=un_amt[username]
    print(f'your current balance is {total_balance}')

vvgroup=True

while vvgroup:
    if username in un_pass.keys():

        if password in un_pass.values():
            print("welcome to hdfc")

            print("select one options")
            print("1.deposite"'\n''2.withdraw''\n''3.check_balance''\n''4.exit')
            choice = input("enter  your choice")
            if choice == '1':
                amt = int(input("enter the amount:"))
                id = int(input("enter upi id:"))
                if amt > 0 and id in un_upi.values():
                    deposite()
                else:
                    print("invalid choice")
            elif choice == '2':
                withdraw_amt = int(input("enter the amount:"))
                id = int(input("enter upi id:"))
                if withdraw_amt > 0 and id in un_upi.values():
                    withdraw()
                elif withdraw_amt < un_amt[username]:
                    print("insufficient Balance")

            elif choice == '3':
                id = int(input("enter your upi id:"))

                if id in un_upi.values():
                    balance_check()

                else:
                    print("your upi id is invalid")
            elif choice=='4':
                print("*************thank you contacting our hdfc bank*************")
                break


    else:
        print("thank u")

        break

