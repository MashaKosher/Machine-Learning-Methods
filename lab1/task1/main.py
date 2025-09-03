from utils import *


if __name__ == "__main__":
    while True:
        print("\n" + "="*50)
        print("ГЛАВНОЕ МЕНЮ")
        print("="*50)
        print("1. Поиск делителей числа")
        print("2. Анализ строки (подсчет слов с четной длиной и самое длинное слово)")
        print("3. Обработка списка (наибольший четный элемент и преобразование)")
        print("4. Поиск ключей с наименьшими значениями в словаре")
        print("5. Выход")
        print("="*50)
        
        choice = input("Выберите задание (1-5): ").strip()
        
        if choice == "1":
            find_divisors()
        elif choice == "2":
            analyze_string()
        elif choice == "3":
            process_list()
        elif choice == "4":
            find_n_smallest()
        elif choice == "5":
            print("Выход из программы...")
            break
        else:
            print("❌ Неверный выбор! Пожалуйста, введите число от 1 до 5")
