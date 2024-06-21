# Принцип работы сортировки вставками:
# 1. Считаем первый элемент списка отсортированным.
# 2. Затем берем следующий элемент и вставляем его на правильное место в уже отсортированной части списка.
# 3. Повторяем этот процесс для каждого элемента, пока весь список не будет отсортирован.
def insertion_sort(arr):
    n = len(arr)
    
    # Проходим по каждому элементу массива
    for i in range(1, n):
        key = arr[i]
        j = i-1
        
        # Сдвигаем все элементы больше ключа на одну позицию вперед
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        # Вставляем ключ в правильное место
        arr[j+1] = key
    
    return arr

# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = insertion_sort(arr)
print(sorted_arr)

def insertion_sort2(arr):
    for i in range(1, len(arr)):
        current_element = arr[i]  # Текущий элемент, который мы хотим вставить
        j = i - 1

        # Сравниваем текущий элемент с элементами в отсортированной части и сдвигаем их, если нужно
        while j >= 0 and current_element < arr[j]:
            arr[j + 1] = arr[j]  # Сдвигаем элемент вправо
            j -= 1

        arr[j + 1] = current_element  # Вставляем текущий элемент на правильное место

# Пример использования
my_list = [5, 2, 9, 1, 5]
insertion_sort2(my_list)
print("Отсортированный список:", my_list)
