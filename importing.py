import csv


def importing():
    print(f'Введите данные через пробел в формате: Имя Фамилия Номер')
    surename = []
    for i in input().split():
        surename.append(i)
    surename = [surename]

    with open('baza_d.csv', 'a', encoding='utf-8', newline='') as file:
        some_str = csv.writer(file)
        # some_list = [[surename, name, numers]]
        for i in surename:
            some_str.writerow(i)
