def imp_exp():
    itemp = False
    while not itemp:
        number = input(f'Выберите действие: \n 1 - экспорт | 2 - импорт \n')
        if number == '1':
            itemp = True
            return True
        elif number == '2':
            itemp = True
            return False
        else:
            print('Введенно неизвестное значение!')
