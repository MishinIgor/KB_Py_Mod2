def merge_sort(arr):
    # Рекурсивная функция сортировки слиянием
    def merge_sort_recursive(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        # Рекурсивно сортируем левую и правую половины
        left = merge_sort_recursive(left)
        right = merge_sort_recursive(right)
        
        # Слияние двух отсортированных половин
        return merge(left, right)
    
    # Функция для слияния двух отсортированных массивов
    def merge(left, right):
        merged = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        # Добавляем оставшиеся элементы из левого и правого массивов
        while i < len(left):
            merged.append(left[i])
            i += 1
        
        while j < len(right):
            merged.append(right[j])
            j += 1
        
        return merged
