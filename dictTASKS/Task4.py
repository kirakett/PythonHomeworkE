"""Создайте словарь с количеством элементов не менее 5-ти.
Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
"""
#Создаем словарь
Dictionary = {'объект1': 'значение объекта 1',
              'объект2': 'значение объекта 2',
              'объект3': 'значение объекта 3',
              'объект4': 'значение объекта 4',
              'объект5': 'значение объекта 5'}

#Создаем второй словарь, чтобы добавить объект 5 и его значение в начало словаря 1
Dictionary2 = {'объект5': 'значение объекта 5'}

#Удаляем наш первый элемент в словаре 1
del Dictionary['объект1']

#Меняем местами словарь 1 и словарь 2
Dictionary, Dictionary2 = Dictionary2, Dictionary

#Из-за перестановки теперь мы можем добавить словарь 2 в начало словаря 1
Dictionary.update(Dictionary2)

#Добавляем объект 1 в конец словаря
Dictionary['объект1'] = 'значение объекта 1'

#По заданию удаляем второй элемент в словаре 1 и добавляем новую пару ключ-значение в конец
del Dictionary['объект2']
Dictionary['новый объект2'] = 'новое значение объекта 2'

print(Dictionary)