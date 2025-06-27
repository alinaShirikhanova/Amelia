# Сделай дз
# Достать из рюкзака
# Посмотреть дз по первому предмету
# Начать его выполнять
# ...

# print() - функция

# define - описать
# def do_homework():
#     print('Достать из рюкзака дневник')
#     print('Посмотреть дз по первому предмету')
#     print('Начать его выполнять')
#     print('...')
#
#
# do_homework()
# do_homework()

def print_card(name):
    print(f'С днем рождения, {name}')


print_card('Амелия')





# print_price
# Печать цены товар
# Товар стоит: <price>

# def print_price(price):
#     print(f'fuggler стоит:{price}')
#
#
# p = int(input('Введите цену товара для ценника: '))
# print_price(p)
# print_price(4373)


# Калькулятор
# def sum(a, b):
#     print(f"Результат суммы: {a + b}")
#
#
# fuggler = int(input())
# labubu = int(input())
# # sum(10, 5)
# sum(fuggler, labubu)








# Реализовать функцию, которая принимает 2 числа:
# - v скорость в км/ч
# - t время (сколько часов ехал)
# Функция должна печатать путь

# def fuggler(a, b):
#     print(f'путь: {a * b}')
#
#
# v = int(input())
# t = int(input())
# fuggler(v, t)
# fuggler(30,5)

# Реализовать функцию, которая принимает число n
# Распечатать все числа от 1 до n включительно

def print_num(n):
    for i in range(1, n + 1):
        print(i)


print_num(3)