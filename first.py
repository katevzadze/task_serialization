file_one = input('Введите название первого файла: ')
file_last = input('Введите название последнего файла: ')
first_number = int(file_one.split('.')[0])
last_number = int(file_last.split('.')[0])
for i in range(first_number, last_number + 1):
    file_name = f'{i}.txt'
    with open(file_name, 'r') as file:
        text = file.read()
        with open('for_buh.txt', 'a') as file_buh:
            file_buh.write(text)
            print(f'Файл {file_name} добавлен в for_buh.txt')
    file.close()
    print(f"Файлы успешно обработаны! Всего {last_number - first_number + 1}.")
