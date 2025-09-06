import pandas as pd

def fill_missing_values(dataFrame: pd.DataFrame) -> pd.DataFrame:
    """
    Заполнение пропусков в данных без обработки выбросов
    """
    print("=" * 60)
    print("ЗАПОЛНЕНИЕ ПРОПУСКОВ В ДАННЫХ")
    print("=" * 60)
    
    df = dataFrame.copy()
    
    # 1. АНАЛИЗ ПРОПУСКОВ ДО ЗАПОЛНЕНИЯ
    print("\n" + "АНАЛИЗ ПРОПУСКОВ ДО ЗАПОЛНЕНИЯ")
    print("-" * 40)
    
    missing_before = df.isnull().sum()
    missing_cols = missing_before[missing_before > 0]
    
    if len(missing_cols) == 0:
        print("Пропусков не обнаружено")
        return df
    else:
        print("Обнаружены пропуски в столбцах:")
        for col, count in missing_cols.items():
            print(f"   {col}: {count} пропусков ({count/len(df)*100:.1f}%)")
    
    # Визуализация пропусков до заполнения
    # analyze_misses(df)

    
    # 2. ЗАПОЛНЕНИЕ ПРОПУСКОВ
    print("\n" + "ПРОЦЕСС ЗАПОЛНЕНИЯ ПРОПУСКОВ")
    print("-" * 40)
    
    # Стратегия заполнения для каждого столбца
    filling_strategy = {
        'Product_Category_2': {
            'method': 'median',
            'value': df['Product_Category_2'].median(),
            'reason': 'Числовая категория, заполняем медианой'
        },
        'Product_Category_3': {
            'method': 'median', 
            'value': df['Product_Category_3'].median(),
            'reason': 'Числовая категория, заполняем медианой'
        }
    }
    

    for col, strategy in filling_strategy.items():
        if col in df.columns and df[col].isnull().sum() > 0:
            if strategy['method'] == 'median':
                fill_value = strategy['value']
                missing_count = df[col].isnull().sum()
                df[col] = df[col].fillna(fill_value)

    return df


def fill_missing_value_mode(df: pd.DataFrame) -> pd.DataFrame:
    """
    Заполнение пропусков в данных.
    """
    print("=" * 60)
    print("ЗАПОЛНЕНИЕ ПРОПУСКОВ В ДАННЫХ")
    print("=" * 60)
    
    data = df.copy()
    
    missing_before = data.isnull().sum()
    missing_cols = missing_before[missing_before > 0]
    
    if missing_cols.empty:
        print("Пропусков не обнаружено")
        return data
    
    print("\nПропуски до заполнения:")
    for col, count in missing_cols.items():
        print(f"   {col}: {count} ({count/len(data)*100:.1f}%)")
    
    # Заполнение
    for col in missing_cols.index:
        # if data[col].dtype == 'object':  
            # категориальные → mode
        fill_value = data[col].mode()[0]
        strategy = 'mode'
        # else:
        #     # числовые → median
        #     fill_value = data[col].median()
        #     strategy = 'median'
        
        data[col] = data[col].fillna(fill_value)
        print(f"   {col} → заполнено методом {strategy}, значение {fill_value}")
    
    return data
