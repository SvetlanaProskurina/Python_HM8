def add_person(data):
    dict = {}
    
    key = input('Введите фамилию, имя, отчество ученика через пробел ')
    val = int(input('Введите оценку ученика '))
    dict[key] = val
    # print(dict)
    
    with open(data, 'a', encoding='utf-8') as f2:
        for key,val in dict.items():
            f2.write('{}\n{}\n'.format(key,val))
            
    print(f'Вы добавили новую запись в журнал {data}: {key} оценка {val}')
# add_person('algebra.txt')