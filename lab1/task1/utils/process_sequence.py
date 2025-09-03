def process_sequence():
    try:
        input_str = input("Введите числа, разделенные запятой: ").strip()
        
        if not input_str:
            print("Пустой ввод!")
            return
        
        numbers_list = [float(x.strip()) for x in input_str.split(',')]
        
        numbers_tuple = tuple(numbers_list)
        
        print(f"\nВведенная последовательность: {input_str}")
        print(f"Список: {numbers_list}")
        print(f"Тип списка: {type(numbers_list)}")
        print(f"Кортеж: {numbers_tuple}")
        print(f"Тип кортежа: {type(numbers_tuple)}")
        
        return numbers_list, numbers_tuple
        
    except ValueError:
        print("Ошибка! Пожалуйста, вводите только числа, разделенные запятыми.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")