class Example:
    static_var1 = 10
    static_var2 = 20
    
    def __init__(self):
        self.dynamic_var1 = 5
        self.dynamic_var2 = 3
        
    def first_method(self):
        local_var = "Hello from first method!"
        print(local_var)
        return local_var
        
    def second_method(self):
        return self.static_var1 + self.static_var2
        
    def third_method(self):
        return self.dynamic_var1 ** self.dynamic_var2
    
    def __str__(self):
        return (
            f"{'=' * 50}\n"
            f"КЛАСС Example\n"
            f"{'=' * 50}\n"
            f"Статические переменные класса:\n"
            f"  static_var1 = {self.static_var1}\n"
            f"  static_var2 = {self.static_var2}\n\n"
            f"Динамические переменные объекта:\n"
            f"  dynamic_var1 = {self.dynamic_var1}\n"
            f"  dynamic_var2 = {self.dynamic_var2}\n\n"
            f"{'=' * 50}"
        )
    

def test_example():
    empl = Example()

    print("=" * 60)
    print("Класс Example")
    print("=" * 60)
    print(empl)
    print("-" * 40)
    
    print("\n1. Первый метод:")
    print("-" * 40)
    print(f"Создает переменную и выводит ее: {empl.first_method()}")

    print("\n2. Второй метод:")
    print("-" * 40)
    print(f"Сумма 2-ух статических переменных: {empl.second_method()}")

    print("\n3. Третий метод:")
    print("-" * 40)
    print(f"Возведение певрой динамической перменной во вторую: {empl.third_method()}")
