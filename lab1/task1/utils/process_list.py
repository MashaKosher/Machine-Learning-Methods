def process_list():
    try:
        input_str = input("Введите элементы списка через пробел: ")
        original_list = list(map(int, input_str.split()))
        
        if not original_list:
            print("Список пустой!")
            return
                
        print(f"\nИсходный список: {original_list}")

        print(f"1. Наибольший четный элемент (или первый): { findMaxOdd(original_list)}")
        
        print(f"2. Список после преобразования: {sorted(original_list, reverse=True)}")
        
    except ValueError:
        print("Ошибка! Пожалуйста, вводите только целые числа.")



def findMaxOdd(nums: list) -> int:
    return max(list(filter(lambda x: x % 2 == 0, nums))) if list(filter(lambda x: x % 2 == 0, nums)) else nums[0]