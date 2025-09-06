from utils import *

if __name__ == "__main__":
    while True:
        print("\n" + "="*50)
        print("ГЛАВНОЕ МЕНЮ")
        print("="*50)
        print("1. Класс Example")
        print("2. Класс Employee")
        print("3. Класс Zoo")
        print("4. Кастосный класс BankAccount с методами экземпляра класса, статическими и класса")
        print("5. Выход")
        print("="*50)
        
        choice = input("Выберите задание (1-5): ").strip()
        
        if choice == "1":
            test_example()
        elif choice == "2":
            test_employee()
        elif choice == "3":
            test_zoo()
        elif choice == "4":
            test_bank()
        elif choice == "5":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор! Пожалуйста, введите число от 1 до 5")
