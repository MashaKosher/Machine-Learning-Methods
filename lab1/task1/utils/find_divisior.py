def find_divisors():
    try:
        number = int(input("Введите целое число: "))
        
        if number == 0:
            print("У числа 0 бесконечно много делителей")
            return
        
        divisors = []
        for i in range(1, abs(number)//2 + 1):
            if number % i == 0:
                if number < 0:
                    divisors.append(-i)
                else:
                    divisors.append(i)

        divisors.append(number)
        
        print(f"Делители числа {number}:")
        print(sorted(divisors))
        
    except ValueError:
        print("Ошибка! Пожалуйста, введите целое число.")