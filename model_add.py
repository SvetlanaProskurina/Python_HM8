def add_new_person(choice, data_student, data_teachers):
    if choice == 4:
        data = data_student
    elif choice == 5:
        data = data_teachers
   
    with open(data, 'a', encoding='utf-8') as f:
        value = (input('Введите данные через пробел\n'))
        if value.__contains__(' '):
            f.write(value)
            f.write('\n')
        else:
            x = value.replace(',', ' ')
            f.write(x)
            f.write('\n')
    print(f'Добавлена новая запись в {data}')
