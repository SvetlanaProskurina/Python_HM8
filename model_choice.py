#To make a choice in the dictionary
import model_admin

def choice(role):
    # role = model_admin.find_login()
    if role == 1: # админ
        choice = int(input('Choose your option: \n'
                    '1 - read all records \n'
                    '2 - read 1 student record \n'
                    '3 - update student record \n'
                    '4 - add new student in base\n'
                    '5 - add new teacher in base\n'
                    '6 - add new student in magazine\n'
                    '\n'))
        return(choice)
    elif role == 2: # учитель
        choice = int(input('Choose your option: \n'
                    '1 - read all records \n'
                    '2 - read 1 student record \n'
                    '3 - update student record \n'
                    '\n'))
        return(choice)
    else: # студент
        choice = int(input('Choose your option: \n'
                    '2 - read 1 student record \n'
                    '\n'))
        return(choice)