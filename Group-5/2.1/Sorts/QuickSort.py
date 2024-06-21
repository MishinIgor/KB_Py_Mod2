def quick_sort(arr):
    # Рекурсивная функция быстрой сортировки
    def quick_sort_recursive(arr, low, high):
        if low < high:
            # Разделяем массив на две части и получаем индекс опорного элемента
            pivot_index = partition(arr, low, high)
            
            # Рекурсивно сортируем левую и правую части массива
            quick_sort_recursive(arr, low, pivot_index - 1)
            quick_sort_recursive(arr, pivot_index + 1, high)
    
    # Функция для разделения массива на две части
    def partition(arr, low, high):
        # Берем последний элемент как опорный
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        # Меняем местами опорный элемент с элементом на позиции i+1
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1
    
    # Вызываем рекурсивную функцию быстрой сортировки
    quick_sort_recursive(arr, 0, len(arr) - 1)

# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
quick_sort(arr)
print(arr)
