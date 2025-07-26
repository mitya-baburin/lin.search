import random
import time
import matplotlib.pyplot as plt    #matplotlib.pyplot— библиотека, используемая для построения графиков

# Определение функции линейного поиска
def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1

sizes = [10, 100, 1000]
times = []

for size in sizes:
    test_list = [random.randint(1, 1000) for _ in range(size)]  # Создаем список случайных чисел
    start_time = time.time()    #Время начала
    linear_search(test_list, random.randint(1, 1000))  # Ищем случайное число
    end_time = time.time()    #Время окончания
    times.append(end_time - start_time)    #Сохраняем разницу времени

for size, duration in zip(sizes, times):
    print(f"Размер списка: {size}, Время выполнения: {duration:.10f} секунд")

#Graphic
plt.plot(sizes, times, marker='o')
plt.title('Время выполнения линейного поиска')
plt.xlabel('Размер списка')
plt.ylabel('Время выполнения (секунд)')
plt.xticks(sizes)
plt.grid()
plt.show()