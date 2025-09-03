from utils import *


if __name__ == "__main__":
    while True:
        print("\n" + "="*50)
        print("ГЛАВНОЕ МЕНЮ")
        print("="*50)
        print("1. Поиск делителей числа")
        print("2. Анализ строки (подсчет слов с четной длиной и самое длинное слово)")
        print("3. Выход")
        print("="*50)
        
        choice = input("Выберите задание (1-3): ").strip()
        
        if choice == "1":
            find_divisors()
        elif choice == "2":
            analyze_string()
        elif choice == "3":
            print("Выход из программы...")
            break
        else:
            print("❌ Неверный выбор! Пожалуйста, введите число от 1 до 3")
