def find_and_reverse_ordered_row(matrix):
    for i, row in enumerate(matrix):
        if is_strictly_increasing(row):
            result = [row_copy[:] for row_copy in matrix]
            result[i] = row[::-1]
            return result, i, True
    
    return matrix, -1, False

def is_strictly_increasing(arr) -> bool:
    if len(arr) <= 1:
        return True
    
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            return False
    return True

def print_matrix(matrix, title="Матрица"):
    print(f"\n{title}:")
    print("+" + "-" * (len(matrix[0]) * 4 - 1) + "+")
    for row in matrix:
        print("| " + " | ".join(f"{x:2d}" for x in row) + " |")
    print("+" + "-" * (len(matrix[0]) * 4 - 1) + "+")


def test_examples():
    test_cases = [
        # Пример 1: Есть упорядоченная строка
        [
            [1, 2, 3, 4],
            [5, 3, 1, 2],
            [9, 8, 7, 6],
            [1, 3, 5, 7]
        ],
        
        # Пример 2: Несколько упорядоченных строк (берется первая)
        [
            [4, 5, 6, 7],
            [1, 2, 3, 4],
            [9, 8, 7, 6],
            [2, 4, 6, 8]
        ],
        
        # Пример 3: Нет упорядоченных строк
        [
            [5, 3, 1, 2],
            [9, 8, 7, 6],
            [4, 2, 4, 6],  # Не строго возрастает (2, 4)
            [1, 1, 2, 3]   # Не строго возрастает (1, 1)
        ],
        
        # Пример 4: Матрица с одним элементом
        [
            [1]
        ],
        
        # Пример 5: Пустая матрица
        []
    ]
    
    for i, matrix in enumerate(test_cases, 1):
        print(f"\n{'='*50}")
        print(f"ТЕСТ {i}")
        print(f"{'='*50}")
        
        if not matrix or not matrix[0]:
            print("Пустая матрица")
            continue
            
        print_matrix(matrix, "Исходная матрица")
        
        result_matrix, row_index, found = find_and_reverse_ordered_row(matrix)
        
        if found:
            print(f"Найдена упорядоченная строка: индекс {row_index}")
            print(f"Строка до реверса: {matrix[row_index]}")
            print(f"Строка после реверса: {result_matrix[row_index]}")
            print_matrix(result_matrix, "Измененная матрица")
        else:
            print("Упорядоченных строк не найдено")
