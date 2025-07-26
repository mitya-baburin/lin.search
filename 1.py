def linear_search(lst, x):
    for index, value in enumerate(lst):
        if value == x:
            return index
    return -1

list = [5, 15, 25]

x_number = 15    # Число, которое будем искать

index = linear_search(list, x_number)    # Поиск числа
# Проверка результата и вывод
if index != -1:
    print(f"{x_number} найдено по индексу {index}.")
else:
    print(f"{x_number} не найдено в списке.")
