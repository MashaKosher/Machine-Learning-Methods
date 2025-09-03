def find_n_smallest(n : int = 3):   
    my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20} 
    print("Исходный словарь:")
    for key, value in my_dict.items():
        print(f"  {key}: {value}")

    sorted_keys = sorted(my_dict, key=lambda x: my_dict[x])[:n]
    
    print(f"\nТри ключа с самыми маленькими значениями: {sorted_keys}")
    print("Соответствующие значения:")
    for key in sorted_keys:
        print(f"  {key}: {my_dict[key]}")