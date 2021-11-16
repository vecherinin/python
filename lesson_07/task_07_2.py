import os

config = os.path.join('.', 'config_2.yaml')
dir = dict()
dir[-1] = os.path.join('.', 'task_07_2')  # Путь для размещения проекта


def create_dir_or_file(level, name):
    """Создать директорию или файл"""
    if name.endswith(':'):
        dir[level] = os.path.join(dir[level-1], name.replace(':', ''))
        if not os.path.exists(dir[level]):
            os.mkdir(dir[level])
    else:
        dir[level] = os.path.join(dir[level-1], name)
        new_file = open(dir[level], 'w', encoding='utf-8')
        new_file.close()


with open(config, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n')
        if line[0:1] != ' ':  # Если без пробела в начале строки
            create_dir_or_file(0, line)
        else:
            lines = line.split('- ')
            level = lines[0].count(' ') // 2  # Уровень вложенности
            dir_name = lines[1]
            create_dir_or_file(level, dir_name)
