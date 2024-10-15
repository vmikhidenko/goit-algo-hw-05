def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        
        # Якщо знаходимо точне значення
        if arr[mid] == target:
            return (iterations, arr[mid])
        
        # Якщо значення більше за цільове
        elif arr[mid] > target:
            upper_bound = arr[mid]
            right = mid - 1
        
        # Якщо значення менше за цільове
        else:
            left = mid + 1
    
    # Якщо точне значення не знайдено, повертаємо найменший елемент, більший або рівний цільовому
    return (iterations, upper_bound)

# Тестуємо двійковий пошук
arr = [1.1, 2.5, 3.3, 5.5, 7.7, 9.9]
target = 4.0
result = binary_search(arr, target)
print(result)  # Наприклад, виведе: (3, 5.5)
