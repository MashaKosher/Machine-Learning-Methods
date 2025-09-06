def demonstrate_try_except_finally():
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ TRY/EXCEPT/FINALLY")
    print("=" * 60)
    
    print("\n1. Нормальное выполнение без ошибок:")
    print("-" * 40)
    try:
        result = 10 / 2
        print(f"Результат деления: {result}")
        print("Код в try блоке выполнен успешно!")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        print("Блок finally выполняется ВСЕГДА (даже если нет ошибок)")

    print("\n2. Обработка конкретного исключения (ZeroDivisionError):")
    print("-" * 40)
    try:
        result = 10 / 0
        print(f"Результат: {result}")
    except ZeroDivisionError:
        print("Поймано исключение: Деление на ноль!")
    except Exception as e:
        print(f"Другая ошибка: {e}")
    finally:
        print("Блок finally выполнен")


    print("\n3. Несколько except блоков:")
    print("-" * 40)
    try:
        number = int("не число")
        result = 10 / number
        print(f"Результат: {result}")
    except ValueError:
        print("Ошибка преобразования строки в число!")
    except ZeroDivisionError:
        print("Ошибка деления на ноль!")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    finally:
        print("Finally блок выполняется всегда")
    
    print("\n4. Общий обработчик исключений:")
    print("-" * 40)
    try:
        my_list = [1, 2, 3]
        print(f"Элемент списка: {my_list[5]}")
    except Exception as e:
        print(f"Поймано исключение: {type(e).__name__} - {e}")
    finally:
        print("Finally: Освобождение ресурсов")