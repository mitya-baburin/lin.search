import random

def linear_search(lst, x):    # Определение функции линейного поиска
    for index, value in enumerate(lst):
        if value == x:
            return index
    return -1

random_list = [random.randint(1, 1000) for _ in range(100)]    # Создаем список из 100 случайных чисел

search_values = [random_list[14], random_list[87], 863, 900]  # Существующие и несуществующие элементы

results = {value: linear_search(random_list, value) for value in search_values}
print("Результаты линейного поиска:", results)