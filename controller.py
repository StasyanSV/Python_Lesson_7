import view
import export
import importing


def click():
    if view.imp_exp():
        name_str = input(f'Введите Имя, Фамилию или номер для поиска:\n  * - выводит всю библиотеку\n')
        export.exporting(name_str)
    else:
        importing.importing()

