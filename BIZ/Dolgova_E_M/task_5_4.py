# Задача 5. Вариант 4.
# Напишите программу, которая при запуске случайным образом отображала один из трех цветов светофора

# Долгова Е.М.
# 15.03.2017

print ("Программа случайным образом отображает один из трех цветов светофора")

import random
stuffing=random.randint (1,3)
if stuffing == 1:
	print ("Красный цвет")
elif stuffing == 2:
	print ("Желтый цвет")
elif stuffing == 3:
	print ("Зеленый цвет")
	
input ("\n\nНажмите Enter  для выхода.")