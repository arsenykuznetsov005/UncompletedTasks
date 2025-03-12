from os import getcwd, listdir, path

dict_of_tasks = {}


def func(current_path: str):
    context = [path.join(current_path, i) for i in listdir(current_path)]

    for i in context:
        if path.isfile(i) and i.endswith('.md'):  # Проверяем, является ли файл - файлом, и оканчивается ли на .md
            with open(file=i, mode='r', encoding='utf-8') as file:
                list_of_lines = []
                count_of_lines = 0

                for line in file:
                    list_of_lines.append(
                        line)  # Можно добавить .rsplit(), так как лишние проблемы могут помешать проверки .endswith()

                    if line.strip().endswith('❌'):
                        if line.startswith('    ') or line.startswith('\t'):
                            print(list_of_lines[count_of_lines - 1], line)
                        else:
                            print(f'Невыполненная задача в одну строку: {line}')

                            # Если воспользоваться функцией repr(), мы увидим, что в конце некоторых строк стоит \n,
                            # strip() же убирает их (он убирает не только символ пробела ` `, но и табуляции `\t` и новой строки `\n`).
                            # После этой операции в конце нашей строки пропадают какие-либо из перечисленных выше символом, и
                            # мы нормально может проверять на `.endswith()`.
                            ### if f'{current_path}{i}' not in dict_of_tasks:
                            ###     dict_of_tasks[f'{current_path}{i}'] = []  # Мы буквально добавляет список как элемент
                            ### dict_of_tasks[f'{current_path}{i}'].append(line.strip())
                            # Оказывается, что на этапе dict_of_tasks[f'{current_path}{i}'] сразу возвращается значение,
                            # и пользуясь этим, мы используем списочный метод `.append()`.

                    count_of_lines += 1

    for i in context:
        if path.isdir(i):
            func(i)


target = getcwd()
func(current_path=target)
# print(dict_of_tasks)
# for file_path, task in dict_of_tasks.items():
#     if len(task) > 1:
#         print(f'Path:\n{file_path}\nTasks:')
#         print(*task, sep='\n', end='\n\n\n')
#     elif len(task) == 1:
#         print(f'Path:\n{file_path}\nTask:')
#         print(*task, sep='\n', end='\n\n\n')
