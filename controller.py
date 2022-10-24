
import model_convert
import model_choice
import model_changemark 
import model_readall
import model_readone
import model_add
import model_admin
import model_add_mag

data_student = 'pupils.csv'
data_teachers = 'teachers.csv'

data = ''
subject = {}


def subject_f():
    
    lesson = 0
    global data, subject
    
    while lesson < 4:       
        lesson = int(input('Enter the lesson you are looking for: \n'
                    '1 - algebra \n'
                    '2 - literature \n'
                    '3 - chemistry \n'
                    '\n'
                    ))   
        if lesson == 1:
            subject = model_convert.convert_to_dict('algebra.txt')
            data = 'algebra.txt'
            break
        if lesson == 2:
            subject = model_convert.convert_to_dict('literature.txt')
            data = 'literature.txt'
            break
        if lesson == 3:
            subject = model_convert.convert_to_dict('literature.txt')
            data = 'chemistry.txt'
            break
    # return(lesson)

            
def programs():
    role = model_admin.find_login()
    if role == 1: # если админ, то выводятся его функции в консоль
                   
        chosen = model_choice.choice(1)
        
        if chosen == 1:
            subject_f()
            model_readall.read_all(subject)            
        
        elif chosen == 2:
            subject_f()
            model_readone.read_one(subject)    
        
        elif chosen == 3:
            subject_f()
            model_changemark.change_mark(subject,data)
            
        
        elif chosen == 4:
            model_add.add_new_person(chosen, data_student, data_teachers)
        
        elif chosen == 5:
            model_add.add_new_person(chosen, data_student, data_teachers)
        
        elif chosen == 6:
            subject_f()
            model_add_mag.add_person(data)
        
        else:
            print('oopsie, your choice is incorrect') 
            
    elif role == 2:
        
        chosen = model_choice.choice(2)
        
        if chosen == 1:
            subject_f()
            model_readall.read_all(subject)   
                     
        elif  chosen == 2:
            subject_f()
            model_readone.read_one(subject) 
               
        elif chosen == 3:
            subject_f()
            model_changemark.change_mark(subject) 
             
        else:
            print('oopsie, your choice is incorrect') 
    else:
        chosen = model_choice.choice(3)  
                 
        if chosen == 2:
            subject_f()
            model_readone.read_one(subject)  
              
        else:
            print('oopsie, your choice is incorrect') 
    
 
