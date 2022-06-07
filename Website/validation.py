def account_number_validation(account_number):
    if account_number:
        if len(str(account_number)) == 10:
            try:
                int(account_number)
                return True

            except ValueError:
                print('Invalid account number, account number should only be a number')
                return False

        else:
            print('Account number should be 10 digits')
            return False

    else:
        print('Account number is a required field')
        return False
