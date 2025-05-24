# a = int(input())
# l = []
# # Заполнение списка
# for _ in range(a):
#     l.append(int(input()))
#
# # Нахождение максимального элемента
# maxi = 0
# maxi_i = 0
# mini_i = 10000000
# mini = 100000
# for i in range(len(l)):
#     if maxi < l[i]:
#         maxi = l[i]
#         maxi_i = i
#     if mini > l[i]:
#         mini = l[i]
#         mini_i = i
# l[mini_i], l[maxi_i] = l[maxi_i], l[mini_i]
# print(l)

l = [1, 2, 3, 4, 5]
la = l[4]
for i in range(4, 0, -1):
    l[i] = l[i - 1]
l[0] = la

print(l)
