import csv


def exporting(name_str):
    with open('baza_d.csv', newline='', encoding='utf-8') as file:
        some_str = csv.reader(file)
        count = 0
        if name_str != '*':
            for i in some_str:
                if name_str in i:
                    print(str(i)[1: - 1])
                    count += 1
        elif name_str == '*':
            for i in some_str:
                print(str(i)[1: - 1])
            count += 1
        if count == 0:
            print('ничего не найдено')
