from os import getcwd, listdir, path

dict_of_tasks = {}


def func(current_path: str):
    context = [path.join(current_path, i) for i in listdir(current_path)]

    for i in context:
        if path.isfile(i) and i.endswith('.md'):  # Проверяем, является ли файл - файлом, и оканчивается ли на .md
            with open(file=i, mode='r', encoding='utf-8') as file:
                file_context = file.readlines()

                for line in file_context:
                    if line.strip().endswith('❌'):
                        if line.startswith('    ') or line.startswith('\t'):
                            if i not in dict_of_tasks:  # Нет ли текущего пути в словаре
                                dict_of_tasks[i] = []  # Добавляет список как элемент
                                dict_of_tasks[i].append(file_context[file_context.index(line) - 1])
                                dict_of_tasks[i].append(line)
                        else:
                            if i not in dict_of_tasks:
                                dict_of_tasks[i] = []  # Добавляет список как элемент
                            dict_of_tasks[i].append(line)

                        # Если воспользоваться функцией repr(), мы увидим, что в конце некоторых строк стоит \n,
                        # strip() же убирает их (он убирает не только символ пробела ` `, но и табуляции `\t` и новой строки `\n`).
                        # После этой операции в конце нашей строки пропадают какие-либо из перечисленных выше символом, и
                        # мы нормально может проверять на `.endswith()`.
                        # if i not in dict_of_tasks:
                        #     dict_of_tasks[i] = []
                        # dict_of_tasks[i].append(line.strip())
                        # Оказывается, что на этапе dict_of_tasks[i] сразу возвращается значение,
                        # и пользуясь этим, мы используем списочный метод `.append()`.

    for i in context:
        if path.isdir(i):
            func(i)


target = getcwd()
func(current_path=target)

with open(file='tasks.md', mode='a', encoding='utf-8') as file:
    for file_path, task in dict_of_tasks.items():
        file.write(f'Путь: `{file_path}`\nПланы:\n')
        for _ in task:
            file.write(_)
        file.write('\n\n\n')
