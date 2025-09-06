from utils import *

if __name__ == "__main__":
    while True:
        print("\n" + "="*50)
        print("ГЛАВНОЕ МЕНЮ")
        print("="*50)
        print("1. Поиск делителей числа")
        print("2. Функция принимающая 1 аргумент")
        print("3. Матрица")
        print("4. Демонстрацию работы try/except/finally")
        print("7. Выход")
        print("="*50)
        
        choice = input("Выберите задание (1-5): ").strip()
        
        if choice == "1":
            find_divisors()
        elif choice == "2":
            test_function()
        elif choice == "3":
            test_examples()
        elif choice == "4":
            demonstrate_try_except_finally()
        elif choice == "5":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор! Пожалуйста, введите число от 1 до 5")
