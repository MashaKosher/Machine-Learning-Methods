def calc_func(data):
    if isinstance(data, list):
        return process_list(data)
    elif isinstance(data, tuple):
        return process_tuple(data)
    elif isinstance(data, int):
        return process_number(data)
    elif isinstance(data, str):
        return process_string(data)
    else:
        return f"Неподдерживаемый тип данных: {type(data).__name__}"
    

def process_list(data: list):
    try:
        zero_indices = []
        for i, item in enumerate(data):
            if item == 0:
                zero_indices.append(i)
                if len(zero_indices) == 2:
                    break

        if len(zero_indices) < 2:
            return("В списке меньше двух нулей")

        start, end = zero_indices[0] + 1, zero_indices[1]
        sublist = data[start:end]
        return sum(sublist)
    except Exception as e:
        return f"Ошибка обработки списка: {e}"


def process_tuple(tpl):
    try:
        if len(tpl) == 0:
            print("Кортеж пуст")
            return

        max_val = max(tpl)
        min_val = min(tpl)

        max_index = tpl.index(max_val)
        min_index = tpl.index(min_val)


        temp_list = list(tpl)


        temp_list[max_index], temp_list[min_index] = temp_list[min_index], temp_list[max_index]


        result_tuple = tuple(temp_list)
        return result_tuple
    except Exception as e:
        return f"Ошибка обработки кортежа: {e}"


def process_number(data:int):
    try:
        return sum([i for i in range(0, data,-1 if data < 0 else 1) if i % 2 == 0])
    except Exception as e:
        return f"Ошибка обработки числа: {e}"
    

def process_string(s:str):
    try:
        return [ord(char) for char in s]

    except Exception as e:
        return f"Ошибка обработки строки: {e}"
    

def test_function():
    test_cases = [
        
        [1, 2, 0, 3, 4, 5, 0, 6, 7],
        [0, 1, 2, 3, 0, 4, 5],
        [1, 2, 3],  
        [0, 0, 1, 2, 3],
        

        (5, 2, 8, 1, 9),
        (10, 20, 30),
        (1,),
        (),
        

        123456,
        2468,
        13579,  
        -2468,
        0,
        
    
        "Hello",
        "123",
        "Привет",
        "🌍✨",    
    ]
    
    print("🧪 ТЕСТИРОВАНИЕ ФУНКЦИИ")
    print("=" * 60)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📋 Тест {i}: {test_case} (тип: {type(test_case).__name__})")
        print("-" * 40)

        print(calc_func(test_case))
