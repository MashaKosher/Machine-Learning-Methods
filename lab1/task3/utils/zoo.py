from abc import ABC, abstractmethod
import json
from typing import List, Dict, Any

class Animal(ABC):    
    def __init__(self, breed: str, price: float):
        self.breed = breed
        self.price = price
    
    @abstractmethod
    def move(self) -> str:
        pass
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.breed}, Цена: {self.price:.2f} руб."
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'type': self.__class__.__name__,
            'breed': self.breed,
            'price': self.price
        }


class Fish(Animal):    
    def move(self) -> str:
        return "Плавает в воде"
    
    def __str__(self) -> str:
        return f"Рыба: {self.breed}, Цена: {self.price:.2f} руб."


class Bird(Animal):
    def move(self) -> str:
        return "Летает по воздуху"
    
    def __str__(self) -> str:
        return f"Птица: {self.breed}, Цена: {self.price:.2f} руб."


class PetShop:
    # Атрибуты класса
    total_shops = 0
    default_discount = 0.1
    shop_types = ["Обычный", "Премиум", "Эксклюзив"]
    
    def __init__(self, name: str, shop_type: str = "Обычный"):
        self.name = name
        self.shop_type = shop_type
        self.animals: List[Animal] = []
        self.founded_year = 2024
        self.total_sales = 0.0
        PetShop.total_shops += 1
    
    def add_animal(self, animal: Animal) -> None:
        self.animals.append(animal)
    
    def get_most_expensive(self) -> Animal:
        if not self.animals:
            raise ValueError("В магазине нет животных")
        
        return max(self.animals, key=lambda x: x.price)
    
    def get_most_expensive_by_type(self, animal_type: type) -> Animal:
        filtered_animals = [a for a in self.animals if isinstance(a, animal_type)]
        
        if not filtered_animals:
            raise ValueError(f"В магазине нет животных типа {animal_type.__name__}")
        
        return max(filtered_animals, key=lambda x: x.price)
    
    def display_all_animals(self) -> None:
        print(f"\n{'='*60}")
        print(f"ЗООМАГАЗИН '{self.name}'")
        print(f"{'='*60}")
        
        if not self.animals:
            print("В магазине нет животных")
            return
        
        for i, animal in enumerate(self.animals, 1):
            print(f"{i}. {animal} -> {animal.move()}")
    
    def display_most_expensive(self) -> None:
        try:
            most_expensive = self.get_most_expensive()
            print(f"\n САМОЕ ДОРОГОЕ ЖИВОТНОЕ:")
            print(f"   {most_expensive}")
            print(f"   Способ передвижения: {most_expensive.move()}")
        except ValueError as e:
            print(e)
    
    def display_most_expensive_fish(self) -> None:
        """Вывести информацию о самой дорогой рыбе"""
        try:
            most_expensive_fish = self.get_most_expensive_by_type(Fish)
            print(f"\n САМАЯ ДОРОГАЯ РЫБА:")
            print(f"   {most_expensive_fish}")
            print(f"   Способ передвижения: {most_expensive_fish.move()}")
        except ValueError as e:
            print(e)
    
    def display_most_expensive_bird(self) -> None:
        """Вывести информацию о самой дорогой птице"""
        try:
            most_expensive_bird = self.get_most_expensive_by_type(Bird)
            print(f"\n САМАЯ ДОРОГАЯ ПТИЦА:")
            print(f"   {most_expensive_bird}")
            print(f"   Способ передвижения: {most_expensive_bird.move()}")
        except ValueError as e:
            print(e)
    
    def save_to_file(self, filename: str) -> None:
        """Сохранить информацию о животных в файл"""
        try:
            data = {
                'pet_shop_name': self.name,
                'animals': [animal.to_dict() for animal in self.animals]
            }
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            print(f"\nИнформация сохранена в файл: {filename}")
            
        except Exception as e:
            print(f"Ошибка при сохранении в файл: {e}")
    
    # ==================== МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА ====================
    
    def sell_animal(self, animal: Animal) -> str:
        """Продать животное (удалить из списка и добавить к продажам)"""
        if animal in self.animals:
            self.animals.remove(animal)
            self.total_sales += animal.price
            return f"Животное {animal.breed} продано за {animal.price:.2f} руб."
        return "Животное не найдено в магазине"
    
    def apply_discount(self, animal: Animal, discount_percent: float) -> float:
        """Применить скидку к цене животного"""
        if animal in self.animals:
            discount_amount = animal.price * (discount_percent / 100)
            animal.price -= discount_amount
            return animal.price
        raise ValueError("Животное не найдено в магазине")
    
    def get_animals_by_price_range(self, min_price: float, max_price: float) -> List[Animal]:
        """Получить животных в определенном ценовом диапазоне"""
        return [animal for animal in self.animals 
                if min_price <= animal.price <= max_price]
    
    def get_total_inventory_value(self) -> float:
        """Получить общую стоимость всех животных в магазине"""
        return sum(animal.price for animal in self.animals)
    
    def get_shop_info(self) -> str:
        """Получить полную информацию о магазине"""
        return (f"Магазин: {self.name}\n"
                f"Тип: {self.shop_type}\n"
                f"Год основания: {self.founded_year}\n"
                f"Количество животных: {len(self.animals)}\n"
                f"Общая стоимость товара: {self.get_total_inventory_value():.2f} руб.\n"
                f"Общие продажи: {self.total_sales:.2f} руб.")
    
    # ==================== МЕТОДЫ КЛАССА ====================
    
    @classmethod
    def get_total_shops(cls) -> int:
        """Получить общее количество созданных магазинов"""
        return cls.total_shops
    
    @classmethod
    def create_premium_shop(cls, name: str) -> 'PetShop':
        """Создать премиум магазин с предустановленными животными"""
        shop = cls(name, "Премиум")
        # Добавляем премиальных животных
        shop.add_animal(Fish("Араван", 15000.0))
        shop.add_animal(Bird("Какаду", 25000.0))
        return shop
    
    @classmethod
    def create_budget_shop(cls, name: str) -> 'PetShop':
        """Создать бюджетный магазин с недорогими животными"""
        shop = cls(name, "Обычный")
        # Добавляем бюджетных животных
        shop.add_animal(Fish("Гуппи", 200.0))
        shop.add_animal(Bird("Волнистый попугай", 800.0))
        return shop
    
    @classmethod
    def set_default_discount(cls, discount: float) -> None:
        """Установить скидку по умолчанию для всех магазинов"""
        cls.default_discount = discount
    
    @classmethod
    def get_shop_types(cls) -> List[str]:
        """Получить список доступных типов магазинов"""
        return cls.shop_types.copy()
    
    # ==================== СТАТИЧЕСКИЕ МЕТОДЫ ====================
    
    @staticmethod
    def validate_price(price: float) -> bool:
        """Проверить корректность цены"""
        return isinstance(price, (int, float)) and price > 0
    
    @staticmethod
    def calculate_tax(price: float, tax_rate: float = 0.18) -> float:
        """Рассчитать налог с продажи"""
        return price * tax_rate
    
    @staticmethod
    def format_price(price: float) -> str:
        """Отформатировать цену для отображения"""
        return f"{price:,.2f} руб."
    
    @staticmethod
    def calculate_discount_price(original_price: float, discount_percent: float) -> float:
        """Рассчитать цену со скидкой"""
        if not (0 <= discount_percent <= 100):
            raise ValueError("Скидка должна быть от 0 до 100%")
        return original_price * (1 - discount_percent / 100)
    
    @staticmethod
    def compare_animals_by_price(animal1: Animal, animal2: Animal) -> str:
        """Сравнить двух животных по цене"""
        if animal1.price > animal2.price:
            return f"{animal1.breed} дороже {animal2.breed} на {animal1.price - animal2.price:.2f} руб."
        elif animal1.price < animal2.price:
            return f"{animal2.breed} дороже {animal1.breed} на {animal2.price - animal1.price:.2f} руб."
        else:
            return f"{animal1.breed} и {animal2.breed} имеют одинаковую цену"
    
    @staticmethod
    def get_animal_category_by_price(price: float) -> str:
        """Определить категорию животного по цене"""
        if price < 1000:
            return "Бюджетное"
        elif price < 5000:
            return "Среднее"
        elif price < 10000:
            return "Дорогое"
        else:
            return "Премиум"


def create_sample_petshop() -> PetShop:
    pet_shop = PetShop("ЗооМир")
    

    pet_shop.add_animal(Fish("Золотая рыбка", 1500.0))
    pet_shop.add_animal(Fish("Скалярия", 2500.0))
    pet_shop.add_animal(Fish("Гуппи", 300.0))
    pet_shop.add_animal(Fish("Дискус", 5000.0))
    

    pet_shop.add_animal(Bird("Волнистый попугай", 2000.0))
    pet_shop.add_animal(Bird("Канарейка", 3500.0))
    pet_shop.add_animal(Bird("Неразлучник", 4500.0))
    pet_shop.add_animal(Bird("Корелла", 6000.0))
    
    return pet_shop


def test_zoo():
    pet_shop = PetShop("ZOO")
    
    while True:
        print(f"\n{'='*60}")
        print("СИСТЕМА УПРАВЛЕНИЯ ЗООМАГАЗИНОМ")
        print(f"{'='*60}")
        print("1. Добавить рыбу")
        print("2. Добавить птицу")
        print("3. Показать всех животных")
        print("4. Найти самое дорогое животное")
        print("5. Найти самую дорогую рыбу")
        print("6. Найти самую дорогую птицу")
        print("7. Сохранить в файл")
        print("8. Демонстрационный пример")
        print("9. Выход")
        
        choice = input("Выберите действие: ").strip()
        
        if choice == '1':
            try:
                breed = input("Введите породу рыбы: ").strip()
                price = float(input("Введите цену: "))
                fish = Fish(breed, price)
                pet_shop.add_animal(fish)
                print(f"Рыба '{breed}' добавлена!")
            except ValueError:
                print("Ошибка ввода цены!")
        
        elif choice == '2':
            try:
                breed = input("Введите породу птицы: ").strip()
                price = float(input("Введите цену: "))
                bird = Bird(breed, price)
                pet_shop.add_animal(bird)
                print(f"Птица '{breed}' добавлена!")
            except ValueError:
                print("Ошибка ввода цены!")
        
        elif choice == '3':
            pet_shop.display_all_animals()
        
        elif choice == '4':
            pet_shop.display_most_expensive()
        
        elif choice == '5':
            pet_shop.display_most_expensive_fish()
        
        elif choice == '6':
            pet_shop.display_most_expensive_bird()
        
        elif choice == '7':
            filename = input("Введите имя файла (например: animals.json): ").strip()
            if filename:
                pet_shop.save_to_file(filename)
        
        elif choice == '8':
            pet_shop = create_sample_petshop()
            print("Загружен демонстрационный пример!")
        
        elif choice == '9':
            print("До свидания!")
            break
        
        else:
            print("Неверный выбор!")



