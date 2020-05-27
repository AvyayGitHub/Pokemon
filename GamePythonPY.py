from time import sleep

def password():
    tries = 3
    while tries >= 0
        pin = int(input("Please Enter Your Pin"))
        if pin == (9187):
            print("Correct!... Fetching Data In A Few Seconds...")
            return True
        else:
            print('Incorrect! Try Again!')
            tries = tries + 1
    print("Incorrect Password And System Is Self Destroying!!!")
    sleep(3)
    return False


def start():
    balance = 1000

    print("Hello, Welcome To The ROBUX(R$) ATM.")
    if password():
        print('1: For Balence')
        print('2: For Withdrawal')
        print('3: For Deposit')
        print('4: For Exit')

        transaction = int(input("Choose Which ROBUX Transaction Fits Your Day: "))
        if transaction == 1
            print('Your Balence Is R$', balance,'\n')