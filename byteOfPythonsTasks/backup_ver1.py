# Program v1

import time
import os

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ["C:\\Users\\Тимур\\Desktop\\Тимурлан\\Программирование\\ex_1", "C:\\Users\\Тимур\\Desktop\\Тимурлан\\Программирование\\ex_2"]

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = "C:\\Users\\Тимур\\Desktop\\Тимурлан\\Программирование\\pup"

# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

# Запускаем создание резервной копии
print(zip_command)
if os.system(zip_command) == 0:
	print('Резервная копия успешно создана в ', targer)
else:
	print('Создание резервной копии НЕ УДАЛОСЬ') 


