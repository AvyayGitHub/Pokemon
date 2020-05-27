from time import sleep

def password():
    tries = 3
    while tries >= 0:
        pin = int(input("Please Enter Your Pin"))
        if pin == (9471):
            print("Correct!... Fetching Data In A Few Seconds...")
            return True
        else:
            print('Incorrect! Try Again!')
            tries = tries + 1
    print("Incorrect Password And System Is Self Destroying!!!")
    sleep(3)
    return False


def start():
    balance = 30000

    print("Hello, Welcome To The ROBUX(R$) ATM.")
    if password():
        print('1: For Balence')
        print('2: For Withdrawal')
        print('3: For Deposit')
        print('4: For Exit')

        transaction = int(input("Choose Which ROBUX Transaction Fits Your Day: "))
        if transaction == 1:
            print('Your Balence Is R$', balance,'\n')
            restart = input("Would You Like To Go Back")
            if restart in('NO', 'no', 'No'):
                print("Thanks For Using R$ ATM. Bye!")

        elif transaction == 2:
            withdrawal = float(input("How much would you like to withdraw?\nR$80\nR$400\nR$800\nR$1000\nR$10000\nR$20000"))
            if withdrawal in[80, 400, 800, 1000, 10000, 20000]:
                balance = balance - withdrawal
                print("Your Balance Is: ", balance)
                restart = input("Would You Like to Go Back?")
                if restart in('NO', 'no', 'No'):
                    print('Thanks For Using R$ ATM. Bye.')
                elif withdrawal != [80, 400, 800, 1000, 10000, 20000]:
                    print("Invalid Amount Try Again.")
                    restart = ('yes', 'YES', 'Yes')


        elif transaction == 3:
            deposit = float(input("How Much R$ Do Ypu Want To Deposit?"))
            balance = deposit + balance
            print("This Is Your Balence In R$:", balance, '\n')

        elif transaction == 4:
            print("Thanks For Using R$ ATM. Bye.")
            print("Exiting Program...")



start()