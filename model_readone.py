#To read just 1 specific record from the dict
from unicodedata import name


def read_one(dic):
    
    student = input('Enter full student name you are looking for: \n')
    if student in dic:
    # if name in dic:
        print(f'{student}, mark {dic[student]}')
        # print(f'{name}, mark {dic[name]}')
    else:
        print('No such student')  