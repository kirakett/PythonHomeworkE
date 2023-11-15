"""
Напишите программу печатающую скидку на поездку в зависимости от набранных баллов.
Программа должна запрашивать количество набранных баллов и печатать сообщение «Ваша скидка:» и скидку:
— от 0 до 49 баллов — «Скидка 10%»;
— от 50 до 99 баллов — «Скидка 15%»;
— от 100 баллов и выше — «Скидка 20%».

Примечание. Наличие функции является обязательным. Функция должна принимать количество набранных баллов.
"""
def count_points(point):
    if point > 0 and point < 49:
        discount = '10%'
    elif point > 49 and point < 99:
        discount = '15%'
    else:
        discount = '20%'
    return discount

print(count_points(int(input('Введите количество баллов: '))))
