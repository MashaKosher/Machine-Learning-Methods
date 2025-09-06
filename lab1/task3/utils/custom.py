class BankAccount:
    bank_name = "Crypto Bank"
    total_accounts = 0
    interest_rate = 0.05

    def __init__(self, owner_name, initial_balance=0):
        self.owner_name = owner_name
        self.balance = initial_balance
        self.account_number = self._generate_account_number()
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        if amount <= 0:
            return "Сумма должна быть положительной"
        self.balance += amount
        return f"Счет пополнен на {amount}. Баланс: {self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Сумма должна быть положительной"
        if amount > self.balance:
            return "Недостаточно средств"
        self.balance -= amount
        return f"Снято {amount}. Баланс: {self.balance}"

    def get_info(self):
        return (f"Владелец: {self.owner_name}\n"
                f"Номер счета: {self.account_number}\n"
                f"Баланс: {self.balance}\n"
                f"Банк: {self.bank_name}")

    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        return f"Новая процентная ставка: {new_rate * 100}%"

    @classmethod
    def get_total_accounts(cls):
        return f"Всего счетов в банке: {cls.total_accounts}"

    @classmethod
    def create_premium_account(cls, owner_name):
        return cls(owner_name, initial_balance=1000)

    @staticmethod
    def validate_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0

    @staticmethod
    def calculate_interest(principal, years, rate):
        return principal * (1 + rate) ** years - principal

    @staticmethod
    def format_currency(amount):
        return f"{amount:,.2f} ₽"

    def _generate_account_number(self):
        return f"PY{BankAccount.total_accounts + 1:06d}"


def test_bank():
    print("ДЕМОНСТРАЦИЯ РАБОТЫ КЛАССА BankAccount")
    print("=" * 50)
    
    account1 = BankAccount("Иван Иванов", 1000)
    account2 = BankAccount("Мария Петрова", 500)
    
    print("ИНФОРМАЦИЯ О СЧЕТАХ:")
    print(account1.get_info())
    print()
    print(account2.get_info())
    
    print("\nОПЕРАЦИИ СО СЧЕТОМ:")
    print(account1.deposit(300))
    print(account1.withdraw(200))
    print(account1.withdraw(2000))
    
    print("\nМЕТОДЫ КЛАССА:")
    print(BankAccount.get_total_accounts())
    print(BankAccount.change_interest_rate(0.07))
    
    premium_account = BankAccount.create_premium_account("Алексей Сидоров")
    print(f"\nПРЕМИУМ СЧЕТ: {premium_account.get_info()}")
    
    print("\nСТАТИЧЕСКИЕ МЕТОДЫ:")
    amount = 1500
    print(f"Валидность суммы {amount}: {BankAccount.validate_amount(amount)}")
    
    interest = BankAccount.calculate_interest(10000, 3, BankAccount.interest_rate)
    print(f"Проценты за 3 года: {BankAccount.format_currency(interest)}")
    
    formatted = BankAccount.format_currency(1234567.89)
    print(f"Форматированная сумма: {formatted}")
