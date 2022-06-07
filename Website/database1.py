import os

# create record
# read record
# update record
# delete record
# This is usually called  CRUD operation
# search for user
import validation

user_data_path = "data/user_record/"

def create(user_account_number, user_details):
    completion_state = False

    try:
        f = open(f"data/user_record/{user_account_number}.txt", "x")

    except FileExistsError:

        print(f'user ({user_account_number})already exists')
        #delete(account_number)

    else:
        f.write(str(user_details))
        completion_state = True
        f.close()
        return completion_state


    # create a file with name 'account number.txt'
    # add user details to the file
    # return True


def read(user_account_number):
    is_account_number_valid = validation.account_number_validation(user_account_number)
    try:
        if is_account_number_valid:
            f = open(f"{user_data_path}{user_account_number}.txt", "r")
        else:
            f = open(f"data/user_record/{user_account_number}", "r")

    except FileNotFoundError:
        print('User not found')

    except FileExistsError:
        print('User does not exist')

    except TypeError:
        print('Invalid account number format')

    else:
        return f.readline()
    # find user record with account number
    # fetch file content


def update(user_account_number):
    print('update user record')
    # find user record with account number
    # fetch file content
    # update the content of the file
    # save the file
    # return True


def delete(user_account_number):
    is_delete_successful = False
    #if os.path.exist(f"{user_data_path}/{user_account_number}.txt"):
    try:
        os.remove(f"{user_data_path}{user_account_number}.txt")
        is_delete_successful = True

    except FileNotFoundError:
        print("User not found")

    finally:
        return is_delete_successful
    # find user with account number
    # delete user's file
    # return true


def does_email_exist(user_account_number, user_email):
    all_users = os.listdir(user_data_path)

    for user in all_users:
        user_data = read(user.removesuffix('.txt'))
        type(user_data)
        if user_email == user_data[1]:
            return True
        else:
            return False







    # find user record with account number
    # return user record as 'file name'


print(does_email_exist(8898574635,'toltom2004@gmail.com'))