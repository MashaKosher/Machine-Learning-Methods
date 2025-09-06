class Employee:
    def __init__(self, full_name="", experience=0, hourly_rate=0, hours_worked=0):
        self.full_name = full_name
        self.experience = experience
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.salary = 0
        self.bonus = 0
        self.total_income = 0
    
    def calculate_salary(self):
        self.salary = self.hourly_rate * self.hours_worked
        return self.salary
    
    def calculate_bonus(self):
        if self.experience < 1:
            bonus_percent = 0.01  
        elif self.experience < 3:
            bonus_percent = 0.05  
        elif self.experience < 5:
            bonus_percent = 0.08  
        else:
            bonus_percent = 0.15  
        
        self.bonus = self.salary * bonus_percent
        return self.bonus
    
    def calculate_total_income(self):
        self.calculate_salary()
        self.calculate_bonus()
        self.total_income = self.salary + self.bonus
        return self.total_income
    
    def __str__(self):
        """Красивое строковое представление сотрудника"""
        return (
            f"\n{'='*60}\n"
            f"ИНФОРМАЦИЯ О СОТРУДНИКЕ\n"
            f"{'='*60}\n"
            f"ФИО: {self.full_name}\n"
            f"Стаж: {self.experience} лет\n"
            f"Часовая ставка: {self.hourly_rate:.2f} руб./час\n"
            f"Отработано часов: {self.hours_worked}\n"
            f"{'-'*60}\n"
            f"Заработная плата: {self.salary:.2f} руб.\n"
            f"Премия ({self.get_bonus_percent()*100}%): {self.bonus:.2f} руб.\n"
            f"ОБЩИЙ ДОХОД: {self.total_income:.2f} руб.\n"
            f"{'='*60}"
        )
    
    def get_bonus_percent(self):
        if self.experience < 1:
            return 0.01
        elif self.experience < 3:
            return 0.05
        elif self.experience < 5:
            return 0.08
        else:
            return 0.15
    
    def display_info(self):
        print(self.__str__())


def input_employee():
    print(f"\n{'='*50}")
    print("ВВОД ДАННЫХ СОТРУДНИКА")
    print(f"{'='*50}")
    
    full_name = input("Введите ФИО сотрудника: ").strip()
    
    while True:
        try:
            experience = float(input("Введите стаж работы (лет): "))
            if experience < 0:
                print("Стаж не может быть отрицательным!")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите число!")
    
    while True:
        try:
            hourly_rate = float(input("Введите часовую ставку (руб.): "))
            if hourly_rate <= 0:
                print("Ставка должна быть положительной!")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите число!")
    
    while True:
        try:
            hours_worked = float(input("Введите количество отработанных часов: "))
            if hours_worked < 0:
                print("Часы не могут быть отрицательными!")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите число!")
    
    # Создаем объект сотрудника
    employee = Employee(full_name, experience, hourly_rate, hours_worked)
    employee.calculate_total_income()
    
    return employee


def input_employees():
    employees = []
    
    print("ПРОГРАММА ДЛЯ РАСЧЕТА ЗАРПЛАТЫ СОТРУДНИКОВ")
    print("=" * 60)
    
    while True:
        try:
            count = int(input("\nСколько сотрудников хотите добавить? "))
            if count <= 0:
                print("Количество должно быть положительным!")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")
    
    for i in range(count):
        print(f"\nСОТРУДНИК {i+1} из {count}")
        employee = input_employee()
        employees.append(employee)
    
    return employees


def display_all_employees(employees):
    """Вывод информации о всех сотрудниках"""
    if not employees:
        print("\nСписок сотрудников пуст!")
        return
    
    print(f"\n{'='*80}")
    print(f"ОТЧЕТ ПО ВСЕМ СОТРУДНИКАМ")
    print(f"{'='*80}")
    
    total_company_salary = 0
    total_company_bonus = 0
    total_company_income = 0
    
    for i, employee in enumerate(employees, 1):
        print(f"\n[{i}] {employee.full_name}")
        print(f"   Стаж: {employee.experience} лет | Ставка: {employee.hourly_rate} руб./час")
        print(f"   Отработано: {employee.hours_worked} часов")
        print(f"   Зарплата: {employee.salary:.2f} руб.")
        print(f"   Премия: {employee.bonus:.2f} руб. ({employee.get_bonus_percent()*100}%)")
        print(f"   ОБЩАЯ СУММА: {employee.total_income:.2f} руб.")
        print(f"   {'-'*40}")
        
        total_company_salary += employee.salary
        total_company_bonus += employee.bonus
        total_company_income += employee.total_income
    
    print(f"\n{'='*80}")
    print(f"ИТОГО ПО КОМПАНИИ:")
    print(f"Общая зарплата: {total_company_salary:.2f} руб.")
    print(f"Общая премия: {total_company_bonus:.2f} руб.")
    print(f"ОБЩИЕ РАСХОДЫ: {total_company_income:.2f} руб.")
    print(f"{'='*80}")


def test_employee():
    employees = []
    
    while True:
        print(f"\n{'='*60}")
        print("ГЛАВНОЕ МЕНЮ")
        print(f"{'='*60}")
        print("1. Добавить сотрудников")
        print("2. Показать всех сотрудников")
        print("3. Показать подробную информацию о сотруднике")
        print("4. Выход")
        
        choice = input("Выберите действие (1-4): ").strip()
        
        if choice == '1':
            new_employees = input_employees()
            employees.extend(new_employees)
            print(f"\nДобавлено {len(new_employees)} сотрудников!")
            
        elif choice == '2':
            display_all_employees(employees)
            
        elif choice == '3':
            if not employees:
                print("\nСначала добавьте сотрудников!")
                continue
            
            print(f"\nСписок сотрудников:")
            for i, emp in enumerate(employees, 1):
                print(f"{i}. {emp.full_name}")
            
            try:
                index = int(input("Выберите номер сотрудника: ")) - 1
                if 0 <= index < len(employees):
                    employees[index].display_info()
                else:
                    print("Неверный номер!")
            except ValueError:
                print("Пожалуйста, введите число!")
                
        elif choice == '4':
            print("\nДо свидания!")
            break
            
        else:
            print("Неверный выбор! Попробуйте снова.")