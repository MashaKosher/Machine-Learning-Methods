def jewelry_shop():
    jewelry_dict = {
        'Кольцо': ['золото, бриллианты', 15000, 5],
        'Серьги': ['серебро, жемчуг', 8000, 8],
        'Цепочка': ['белое золото', 12000, 3],
        'Браслет': ['золото, сапфиры', 25000, 2],
        'Подвеска': ['серебро, изумруд', 6000, 10],
        'Часы': ['сталь, золото, кожа', 35000, 4]
    }
    
    cart = [] 
    
    while True:
        print("\n" + "="*50)
        print("ЮВЕЛИРНЫЙ МАГАЗИН")
        print("="*50)
        print("1. Просмотр описания")
        print("2. Просмотр цены")
        print("3. Просмотр количества")
        print("4. Вся информация")
        print("5. Покупка")
        print("6. До свидания")
        print("="*50)
        
        choice = input("Выберите пункт меню (1-6): ").strip()
        
        if choice == "1":
            view_descriptions(jewelry_dict)
        elif choice == "2":
            view_prices(jewelry_dict)
        elif choice == "3":
            view_quantities(jewelry_dict)
        elif choice == "4":
            view_all_info(jewelry_dict)
        elif choice == "5":
            cart = make_purchase(jewelry_dict, cart)
        elif choice == "6":
            print("До свидания! Спасибо за посещение нашего магазина!")
            break
        else:
            print("Неверный выбор! Пожалуйста, введите число от 1 до 6")

def view_descriptions(jewelry_dict):
    print("\n" + "-"*40)
    print("ОПИСАНИЯ ИЗДЕЛИЙ")
    print("-"*40)
    for name, info in jewelry_dict.items():
        print(f"{name} – {info[0]}")
    print("-"*40)

def view_prices(jewelry_dict):
    print("\n" + "-"*40)
    print("ЦЕНЫ ИЗДЕЛИЙ")
    print("-"*40)
    for name, info in jewelry_dict.items():
        print(f"{name} – {info[1]} руб.")
    print("-"*40)

def view_quantities(jewelry_dict):
    print("\n" + "-"*40)
    print("НАЛИЧИЕ ИЗДЕЛИЙ")
    print("-"*40)
    for name, info in jewelry_dict.items():
        print(f"{name} – {info[2]} шт.")
    print("-"*40)

def view_all_info(jewelry_dict):
    print("\n" + "-"*60)
    print("ВСЯ ИНФОРМАЦИЯ ОБ ИЗДЕЛИЯХ")
    print("-"*60)
    print(f"{'Название':<15} {'Состав':<25} {'Цена':<10} {'Кол-во':<6}")
    print("-"*60)
    
    for name, info in jewelry_dict.items():
        print(f"{name:<15} {info[0]:<25} {info[1]:<10} {info[2]:<6}")
    print("-"*60)

def make_purchase(jewelry_dict, cart):
    print("\n" + "-"*40)
    print("ПОКУПКА")
    print("-"*40)
    print("Введите название изделия и количество через пробел")
    print("Для выхода введите 'n'")
    print("-"*40)
    
    total_cost = 0
    
    while True:
        print("\nДоступные товары:")
        for name, info in jewelry_dict.items():
            if info[2] > 0:
                print(f"  {name} - {info[2]} шт. по {info[1]} руб.")
        
        user_input = input("\nВведите название и количество (или 'n' для выхода): ").strip()
        
        if user_input.lower() == 'n':
            break
        
        try:
            parts = user_input.split()
            if len(parts) < 2:
                print("Ошибка! Введите название и количество через пробел")
                continue
            
            quantity = int(parts[-1])  
            product_name = ' '.join(parts[:-1])  
            
            
            if product_name not in jewelry_dict:
                print(f"Товар '{product_name}' не найден!")
                continue
            
            
            available_qty = jewelry_dict[product_name][2]
            if quantity <= 0:
                print("Количество должно быть положительным числом!")
                continue
            
            if quantity > available_qty:
                print(f"Недостаточно товара! Доступно: {available_qty} шт.")
                continue
            
            
            price = jewelry_dict[product_name][1]
            total_item_cost = price * quantity
            
            
            jewelry_dict[product_name][2] -= quantity
            
           
            cart.append((product_name, quantity, total_item_cost))
            
            print(f"Добавлено в корзину: {product_name} - {quantity} шт.")
            print(f"Стоимость: {total_item_cost} руб.")
            
        except ValueError:
            print("Ошибка! Количество должно быть числом")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
    
   
    if cart:
        print("\n" + "="*50)
        print("ИТОГ ПОКУПКИ")
        print("="*50)
        
        total_cost = 0
        for item in cart:
            name, qty, cost = item
            print(f"{name} - {qty} шт. × {cost//qty} руб. = {cost} руб.")
            total_cost += cost
        
        print("-"*50)
        print(f"ОБЩАЯ СТОИМОСТЬ: {total_cost} руб.")
        print("="*50)
    
    return cart