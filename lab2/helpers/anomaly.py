import pandas as pd
import matplotlib.pyplot as plt

def anomaly_find(dataFrame: pd.DataFrame):
    # Выберем числовые колонки для анализа
    numeric_columns_to_analyze = ['Purchase', 'Occupation', 'Marital_Status', 
                   'Product_Category_1', 'Product_Category_2', 'Product_Category_3']

    print("Анализируемые числовые столбцы:", numeric_columns_to_analyze)

    # 1. БАЗОВАЯ СТАТИСТИКА ДЛЯ ВЫЯВЛЕНИЯ АНОМАЛИЙ
    # base_stats_print(dataFrame, numeric_columns_to_analyze)

    # 2. BOXPLOT С ВЫБРОСАМИ ДЛЯ КАЖДОГО СТОЛБЦА ОТДЕЛЬНО
    boxplot_with_throws_visualization(dataFrame, numeric_columns_to_analyze)




# def base_stats_print(dataFrame: pd.DataFrame, numeric_columns_to_analyze: list[str]):
#     print("\n" + "-" * 40)
#     print("БАЗОВАЯ СТАТИСТИКА ЧИСЛОВЫХ СТОЛБЦОВ")
#     print("-" * 40)

#     for col in numeric_columns_to_analyze:
#         if col in dataFrame.columns:
#             print(f"\nColumn: {col}:")
#             print(dataFrame[col].describe())



def boxplot_with_throws_visualization(dataFrame: pd.DataFrame, numeric_columns_to_analyze: list[str]):
    print("\n" + "=" * 60)
    print("ДЕТАЛЬНЫЙ АНАЛИЗ ВЫБРОСОВ ПО ВСЕМ СТОЛБЦАМ")
    print("=" * 60)
    
    # Создаем одну большую фигуру с subplots
    n_cols = min(3, len(numeric_columns_to_analyze))  # максимум 3 колонки в ряду
    n_rows = (len(numeric_columns_to_analyze) + n_cols - 1) // n_cols
    
    _, axes = plt.subplots(n_rows, n_cols, figsize=(18, 6 * n_rows))
    axes = axes.flatten() if n_rows > 1 or n_cols > 1 else [axes]
    
    # Создаем таблицу для статистики
    stats_data = []
    
    for i, col in enumerate(numeric_columns_to_analyze):
        if i < len(axes):
            # Boxplot с выбросами
            bp = axes[i].boxplot(dataFrame[col].dropna(), patch_artist=True, showfliers=True)
            
            # Настраиваем цвета
            for box in bp['boxes']:
                box.set(facecolor='lightcoral', alpha=0.7)
            for median in bp['medians']:
                median.set(color='darkred', linewidth=2)
            
            # Рассчитываем статистику для выбросов
            Q1 = dataFrame[col].quantile(0.25)
            Q3 = dataFrame[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outliers = dataFrame[(dataFrame[col] < lower_bound) | (dataFrame[col] > upper_bound)][col]
            outliers_percentage = len(outliers) / len(dataFrame) * 100
            
            # Сохраняем статистику
            stats_data.append({
                'Колонка': col,
                'Q1': Q1,
                'Медиана': dataFrame[col].median(),
                'Q3': Q3,
                'IQR': IQR,
                'Выбросы': len(outliers),
                '% Выбросов': outliers_percentage,
                'Границы': f'[{lower_bound:.1f}, {upper_bound:.1f}]'
            })
            
            # Добавляем границы на график
            axes[i].axhline(y=lower_bound, color='red', linestyle='--', alpha=0.7, linewidth=1)
            axes[i].axhline(y=upper_bound, color='red', linestyle='--', alpha=0.7, linewidth=1)
            
            axes[i].set_title(f'{col}\nВыбросы: {len(outliers)} ({outliers_percentage:.1f}%)', 
                             fontsize=11, fontweight='bold')
            axes[i].set_ylabel('Значения', fontsize=9)
            axes[i].tick_params(axis='x', labelsize=8)
            axes[i].tick_params(axis='y', labelsize=8)
            axes[i].grid(True, alpha=0.3)
            
            # Добавляем аннотацию с основными цифрами
            textstr = f'Q1: {Q1:.1f}\nМед: {dataFrame[col].median():.1f}\nQ3: {Q3:.1f}'
            axes[i].text(0.02, 0.98, textstr, transform=axes[i].transAxes, fontsize=8,
                        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    # Скрываем пустые subplots
    for j in range(i + 1, len(axes)):
        axes[j].set_visible(False)
    
    plt.suptitle('АНАЛИЗ ВЫБРОСОВ ПО ВСЕМ ЧИСЛОВЫМ СТОЛБЦАМ', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.subplots_adjust(top=0.93)
    plt.show()
    
    # Выводим сводную таблицу со статистикой
    print("\n" + "-" * 80)
    print("СВОДНАЯ СТАТИСТИКА ВЫБРОСОВ")
    print("-" * 80)
    
    stats_df = pd.DataFrame(stats_data)
    stats_df = stats_df.sort_values('% Выбросов', ascending=False)
    
    # Форматируем вывод для читаемости
    display_df = stats_df.copy()
    display_df['Q1'] = display_df['Q1'].round(2)
    display_df['Медиана'] = display_df['Медиана'].round(2)
    display_df['Q3'] = display_df['Q3'].round(2)
    display_df['IQR'] = display_df['IQR'].round(2)
    display_df['% Выбросов'] = display_df['% Выбросов'].round(2)
    
    print(display_df.to_string(index=False))
    
    # Детальный вывод по каждой колонке
    print("\n" + "-" * 80)
    print("ДЕТАЛЬНЫЙ АНАЛИЗ ПО КОЛОНКАМ")
    print("-" * 80)
    
    for stats in stats_data:
        print(f"\n📊 {stats['Колонка']}:")
        print(f"   Q1: {stats['Q1']:.2f}, Медиана: {stats['Медиана']:.2f}, Q3: {stats['Q3']:.2f}")
        print(f"   IQR: {stats['IQR']:.2f}, Границы: {stats['Границы']}")
        print(f"   Выбросов: {stats['Выбросы']} ({stats['% Выбросов']:.2f}%)")
        
        # Анализируем природу выбросов
        if stats['% Выбросов'] > 10:
            print("     МНОГО ВЫБРОСОВ - требует внимания!")
        elif stats['% Выбросов'] > 5:
            print("     Заметное количество выбросов")
        else:
            print("     Нормальное количество выбросов")