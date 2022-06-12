# My-mini-scripts
Just my dump of my scripts

# AMIS
Add Music In Stellaris (AMIS)
Добавляет пользовательскую музыку в игру Stellaris. 
Обрабатывает музыку только в расширении ".ogg". Если в названии музыки встречается кириллица, то программа предлагает автоматически переименовать файл в латицину. 
Имена с неизвестными символами программа пропускает.

Как добавить музыку в игру:
1) Добавьте свою музыку в папку игры с музыкой (Stellaris\music).
2) Вся музыка должна быть в расширении ".ogg", иное расширение AMIS пропустит.
3) Запустить программу AMIS. Ввести полный путь к папке игры с музыкой (например, C:\Program Files (x86)\Steam\steamapps\common\Stellaris\music)
4) На вопросы отвечать "Y"-yes или "N"-no.

Также программу можно запустить из cmd, в параметре указать полный путь к папке с музыкой без дополнительных знаков.

# renaming_images
Renames all pictures of the format .jpg, .png in a folder in the format: 000, 001, 002, etc.

run: python3 renaming_images.py \[PATH]

PATH: path to the directory with pictures (by default - the current directory)

# resizing_images
Changes the size of all pictures of the format .jpg, .png in a folder and saves the new image to the /new_images folder

run: python3 resizing_images.py WIDTH HEIGHT \[PATH]

WIDTH: width of new pictures
HEIGHT: height of new pictures
PATH: path to the directory with pictures (by default - the current directory)

# top_vk_users
Displays the top users by posts in the group

run: python3 top_vk_users.py
