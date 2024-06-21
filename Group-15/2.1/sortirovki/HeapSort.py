def heap_sort(arr):
    n = len(arr)
    
    # Строим max-кучу из массива
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Извлекаем элементы из кучи по одному и приводим массив к отсортированному виду
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # Меняем максимальный элемент с последним
        heapify(arr, i, 0)                # Восстанавливаем свойство max-кучи для уменьшенной кучи

# Функция для приведения поддерева с корнем i в max-кучу
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Если левый дочерний элемент больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Если правый дочерний элемент больше корня
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # Если корень не является наибольшим элементом, меняем местами корень и наибольший элемент
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        
        # Рекурсивно вызываем heapify для наибольшего элемента
        heapify(arr, n, largest)

# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
heap_sort(arr)
print(arr)
