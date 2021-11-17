# Создать структуру файлов и папок, как написано в задании 2
# (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates:
#
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
#
# Техническое задание
#     1. В папках mainapp, authapp и аналогичных могут быть и другие файлы, кроме приведенных в примере.
#     2. Папку templates надо создать внутри исходной директории, в примере - внутри my_project
#     3. Шаблон - это папка template. Ее уровень в структуре папок может быть любым.
#     4. Исходные файлы и папки необходимо оставить; обратите внимание,
#     что html-файлы расположены в родительских папках (они играют роль пространств имён).
#     5. Предусмотреть возможные исключительные ситуации;
#     это реальная задача, которая решена, например, во фреймворке django.

import os
from shutil import copytree

tpl = 'templates'
path = os.path.join('.', 'task_07_3', 'my_project')
dst = os.path.join(path, tpl)

for root, dirs, files in os.walk(path):
    for dir in dirs:
        root_dir = os.path.join(root, dir)
        if tpl in root_dir and files:
            copytree(root_dir, dst, dirs_exist_ok=True)
