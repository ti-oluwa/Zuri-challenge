import random
import validation
import database1




#database = {
#2925512817 : ['Afolayan Daniel Toluwalase', 'tholuwa2003@zuri.team','toltom', 34500000]
#}


def register():
    print('REGISTER NOW')
    email = str(input("Enter your email address> \n "))
    firstname =str(input("Firstname> \n"))
    lastname = str(input("Lastname> \n"))
    other_name = str(input('Other name> \n'))
    username = lastname + ' ' + firstname + ' ' + other_name
    password = input("Create a password (Password must be atleast 6 characters long and should include special characters & number for a stronger password)> \n")
    account_number = generate_account_number()

    is_user_created = database1.create(account_number, [username, email, password, 0])

    if is_user_created is True:
        print("Your account has been Created")
        print(f"Your Account Number is {account_number}")
        print('                                         \n')
        print('                                         \n')
        q_a = str(input('Do you want to login? (y for yes / n for no)> '))
        is_valid = False
        while is_valid is False:
            if q_a.lower() == 'y':
                is_valid = True
                login()
            elif q_a.lower() == 'n':
                is_valid = False
                print('Thanks for Creating an Account with us')
                print('                          \n')
                register()

            else:
                is_valid = False
                print('Invalid response \n')
                print('y for yes / n for no')
    else:
        print('Something went wrong, please try again')
        register()

def login():
    print('LOGIN')
    print('Enter required details')
    is_login_successful = False
    while is_login_successful is False:

        account_number_from_user = input("What is your account number> \n")
        is_account_number_valid = validation.account_number_validation(account_number_from_user)

        if is_account_number_valid:
            password = str(input('Enter your password> \n'))

            for account_number,user_details in database.items():
                if int(account_number_from_user) == account_number:
                    if user_details[2] == password:
                        print('Login Successful!')
                        bank_operation(user_details, account_number)
                        is_login_successful = True
                    else :
                        print('Incorrect password')
                        is_login_successful = False






def init():
    print(f'welcome to bankPHP')

    have_account = int(input('Do you have an account with us? 1 for yes / 2 for no \n'))
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print('Invalid input! Try again')
        init()
    

def generate_account_number():
    new_account_no = int(random.randint(1111111111, 9999999999))

    return new_account_no



def is_integer(userinput):
    try:
        int(userinput)
        return True
    except ValueError:
        print('Error! You can only input numbers')
        return False




def bank_operation(user, account):
    print(user[0])
    selected_option = int(input('What would you like to do: (1) deposit (2) withdrawal (3) logout (4) check account balance (5) exit  > \n'))

    if is_integer(selected_option):
        if selected_option == 1:
            deposit(account)
        elif selected_option == 2:
            withdrawal(account)
        elif selected_option == 3:
            logout()
        elif selected_option == 4:
            balance = check_balance(account)
            print(f"Your balance is {balance}")
        elif selected_option == 5:
            exit()
        else:
            print('Invalid option selected')
            bank_operation(user, account)
        is_valid = False
        while is_valid is False:
            selected_option2 = str(input(
                'Do you want to perform another transaction or logout? (1) To perform another transaction (2) logout \n'))
            if selected_option2 == '1':
                bank_operation(user, account)
                is_valid = True
            elif selected_option2 == '2':
                logout()
            elif selected_option2 != '1' or '2':
                print('invalid option')
                is_valid = False
    else:
        bank_operation(user, account)




def withdrawal(account):
    withdrawal_amount = int(input('How much do you want to withdraw? \n'))
    new_balance = less_balance(account, withdrawal_amount)
    print('Withdrawing...')
    print('Take your Cash')
    print(f'Your new account balance is {new_balance}')




def deposit(account):
    deposit_amount = int(input('How much do you want to deposit> \n'))
    add_balance(deposit_amount, account)


def logout():
    print('logging out')
    print('   .................        \n')
    print('You are logged out \n')
    print('                                         \n')
    print('                                         \n')
    print('                                         \n')
    init()


def deposit_in_other_account(amount, your_account):
    receiver_account = input('Enter account no> \n')
    if does_account_exist(receiver_account) is True:
        for account_number, user_details in database.items():
            if your_account == account_number:
                user_details[3] -= amount
        for account_number, user_details in database.items():
            if receiver_account == account_number:
                user_details[3] += amount
                print(f'You sent {amount} to {user_details[0]} with account number {account_number} ')
    elif does_account_exist(receiver_account) is False:
        print('Account does not exist')
        deposit_in_other_account(amount, your_account)


def does_account_exist(account_num):
    for account_number in database.keys():
        if account_num == account_number:
            return True
        else:
            return False


def password_maker():
    password = input("Create a password (Password must be atleast 6 characters long and should include special characters & number for a stronger password)> \n")
    if password:
        if len(password) >= 6:
            for characters in list(password):
                if is_integer(characters):
                    for user_details in database.values():
                        if password == user_details[2]:
                            print('Password already taken, create new password')
                            password_maker()
                        else:
                            return password
                else:
                    print('Password must contain at least a number and/or a special character')
                    password_maker()
        else:
            print('Password must be atleast 6 characters long')

    else:
        print('Password required!')





def check_balance(account):
    for account_number,user_details in database.items():
        if account == account_number:
            account_balance = user_details[3]

            return account_balance


def add_balance(amount, account):
    account_for_deposit = str(input('Where do you want to make your deposit in? (1) your account (2) another account \n'))
    if account_for_deposit == '1':
        for account_number, user_details in database.items():
            if account == account_number:
                user_details[3] += amount
            print(f'Your current account balance is {user_details[3]} naira only')


    elif account_for_deposit == '2':
        deposit_in_other_account(amount, account)

    elif account_for_deposit != "1" or '2':
        print('Invalid option!')
        add_balance(amount, account)


def less_balance(account, amount):
    balance = check_balance(account)
    if amount < balance:
        balance -= amount
        for account_number, user_details in database.items():
                if account == account_number:
                    user_details[3] = balance
                    return balance



init()