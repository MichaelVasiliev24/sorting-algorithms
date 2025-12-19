def quick_sort(arr):
    """Быстрая сортировка (Quick Sort) - эффективная сортировка с разделением"""
    if len(arr) <= 1:
        return arr

    quick_sort_recursive(arr, 0, len(arr) - 1)
    return arr


def quick_sort_recursive(arr, low, high):
    """Рекурсивная часть быстрой сортировки"""
    if low < high:
        pivot_index = _partition(arr, low, high)

        quick_sort_recursive(arr, low, pivot_index - 1)
        quick_sort_recursive(arr, pivot_index + 1, high)


def _partition(arr, low, high):
    """Функция разделения массива - выбирает опорный элемент и переставляет другие (слева - < опорного, справа - > опорного)"""
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
