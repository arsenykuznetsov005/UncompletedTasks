from os import getcwd, listdir, path

dict_of_tasks = {}


def func(current_path: str):
    context = [path.join(current_path, i) for i in listdir(current_path)]

    for i in context:
        if path.isfile(i) and i.endswith('.md'):  # Проверяем, является ли файл - файлом, и оканчивается ли на .md
            with open(file=i, mode='r', encoding='utf-8') as file:
                for line in file:
                    if line.strip().endswith('❌'):
                        # Если воспользоваться функцией repr(), мы увидим, что в конце некоторых строк стоит \n,
                        # strip() же убирает их (он убирает не только символ пробела ` `, но и табуляции `\t` и новой строки `\n`).
                        # После этой операции в конце нашей строки пропадают какие-либо из перечисленных выше символом, и
                        # мы нормально может проверять на `.endswith()`.
                        if i not in dict_of_tasks:  # Проверяем существует ли уже текущий ключ в словаре, значением к-ого является список, чтобы не создавать новый список лишний раз.
                            dict_of_tasks[i] = []  # Мы буквально добавляет список как элемент
                        dict_of_tasks[i].append(line.strip())
                        # Оказывается, что на этапе dict_of_tasks[i] сразу возвращается значение,
                        # и пользуясь этим, мы используем списочный метод `.append()`.

    for i in context:
        if path.isdir(i):
            func(i)


target = getcwd()
func(current_path=target)
print(dict_of_tasks)
