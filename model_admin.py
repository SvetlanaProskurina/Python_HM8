def find_login():
    
    name = input("Введите ваши фамилию, имя, отчество через пробел: ")
    count = 0
    with open("administrators.csv", "r", encoding="UTF-8") as f:
        for line in f:
            if name in line:
                print("Вы являетесь администратором")
                role = 1
                return role
                
    with open("teachers.csv", "r", encoding="UTF-8") as f:
        for line in f:
            if name in line:
                print("Вы являетесь учителем")
                role = 2
                return role
                
    with open("pupils.csv", "r", encoding="UTF-8") as f:
        for line in f:
            if name in line:
                print("Вы являетесь учеником")
                role = 3
                return role
                
    if name == 4:
        count += 1
    else:
        print("Вы ввели с ошибкой или не зарегистрированы в системе, обратитесь к администратору")
