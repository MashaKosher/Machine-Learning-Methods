import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def analyze_misses(df: pd.DataFrame, rows_num: int = 1000):
    """
    Анализ пропсуков и постороение графиков (теаловая карта и столбчатая диаграмма)
    
    Args:
        df: pd.DataFrame
        rows_num: кол-во строк для вывода на диаграмме (по умолчанию 1000)
        
    Returns:
        None
    """
    # Подсчет пропусков в каждом столбце
    missing_values = df.isnull().sum()
    missing_percentage = (df.isnull().sum() / len(df)) * 100

    # Создаем датафрейм для наглядности
    missing_df = pd.DataFrame({
        'Количество пропусков': missing_values,
        'Процент пропусков': missing_percentage
    })

    # 2. ВИЗУАЛИЗАЦИЯ ПРОПУСКОВ
    print("\n" + "=" * 50)
    print("ВИЗУАЛИЗАЦИЯ ПРОПУСКОВ")
    print("=" * 50)

    # Создаем фигуру с несколькими графиками
    _, axes = plt.subplots(2, 1, figsize=(14, 10))

    # График 1: Столбчатая диаграмма процента пропусков
    bars = axes[0].bar(missing_df.index, missing_df['Процент пропусков'], 
                      color='skyblue', edgecolor='black')
    axes[0].set_title('Процент пропусков данных по столбцам', fontsize=16, fontweight='bold')
    axes[0].set_ylabel('Процент пропусков (%)', fontsize=12)
    axes[0].tick_params(axis='x', rotation=45)

    # Добавляем значения на столбцы
    for bar in bars:
        height = bar.get_height()
        if height > 0:  # Подписываем только те столбцы, где есть пропуски
            axes[0].text(bar.get_x() + bar.get_width()/2., height + 0.5,
                        f'{height:.1f}%', ha='center', va='bottom')


    # График 2: Тепловая карта пропусков
    # Берем только первые 1000 строк для наглядности (иначе может быть слишком много)
    sns.heatmap(df.head(rows_num).isnull(), cbar=True, 
                yticklabels=False, cmap='viridis', ax=axes[1])
    axes[1].set_title(f'Тепловая карта пропусков (первые {rows_num} строк)', fontsize=16, fontweight='bold')

    plt.tight_layout()
    plt.show()