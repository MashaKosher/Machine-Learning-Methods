import helpers

if __name__ == "__main__":
    helpers.setup()
    dataFrame = helpers.load_data("./train.csv")
    
    while True:
        print("\n" + "="*50)
        print("ГЛАВНОЕ МЕНЮ")
        print("="*50)
        print("1. Первичный аналих данных")
        print("2. Анализируемые столбцы")
        print("3. Столбцы с пропусками")
        print("4. Проверить данные на пропуски")
        print("5. Проверить данные на наличие аномальных значений")
        print("6. Заполнение пустых значений")
        print("7. Испарвление аномалий")
        print("0. Выход")
        print("="*50)
        
        choice = input("Выберите задание (1-7): ").strip()
        
        if choice == "1":
            print(dataFrame.info())
        elif choice == "2":
           print(helpers.get_numeric_columns(dataFrame))
        elif choice == "3":
            helpers.get_columns_with_misses(dataFrame)
        elif choice == "4":
            helpers.analyze_misses(dataFrame)
        elif choice == "5":
            helpers.anomaly_find(dataFrame)
        elif choice == "6":
            helpers.analyze_misses(dataFrame)
            tempDf = helpers.fill_missing_values(dataFrame)
            helpers.analyze_misses(tempDf)
        elif choice == "7":
            helpers.anomaly_find(dataFrame)
            tempDf = helpers.remove_outliers(dataFrame)
            helpers.anomaly_find(tempDf)
        elif choice == "0":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор! Пожалуйста, введите число от 1 до 7")