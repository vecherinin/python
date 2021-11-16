# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp

import os

parent_dir = 'task_07_1'
new_dirs = (
    'my_project', (
        'settings',
        'mainapp',
        'adminapp',
        'authapp'
    )
)

for each in new_dirs[1]:
    dir_path = os.path.join('.', parent_dir, new_dirs[0], each)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
