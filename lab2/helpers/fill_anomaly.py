import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from .helpers import get_numeric_columns

def remove_outliers(dataFrame: pd.DataFrame, method: str = 'capping'):
    """
    Устранение выбросов в числовых данных с выбором метода обработки
    
    Parameters:
    -----------
    dataFrame : pd.DataFrame
        Исходный DataFrame с данными
    method : str, optional (default='capping')
        Метод обработки выбросов:
        - 'capping': Ограничение выбросов по методу IQR (рекомендуется)
        - 'winsorize': Ограничение выбросов перцентилями
        - 'remove': Удаление строк с выбросами
        - 'log': Логарифмическое преобразование
    show_plots : bool, optional (default=True)
        Показывать ли графики до/после обработки
    """
    
    print("=" * 70)
    print("🔧 УСТРАНЕНИЕ ВЫБРОСОВ")
    print("=" * 70)
    
    df = dataFrame.copy()
    original_shape = df.shape
    print(f"Исходный размер данных: {original_shape}")
    print(f"Выбранный метод: {method}")
    
    numeric_columns = [col for col in get_numeric_columns(df) if col in df.columns]
    
    print(f"\nАнализируемые числовые колонки: {numeric_columns}")
    
    # 2. АНАЛИЗ ВЫБРОСОВ ДО ОБРАБОТКИ
    print("\n" + "АНАЛИЗ ВЫБРОСОВ ДО ОБРАБОТКИ")
    print("-" * 40)
    
    outliers_info = {}
    
    for col in numeric_columns:
        if df[col].dtype in ['int64', 'float64']:
            # Метод IQR для обнаружения выбросов
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outliers_mask = (df[col] < lower_bound) | (df[col] > upper_bound)
            outliers_count = outliers_mask.sum()
            
            if outliers_count > 0:
                outliers_info[col] = {
                    'before': outliers_count,
                    'percentage': outliers_count / len(df) * 100,
                    'lower_bound': lower_bound,
                    'upper_bound': upper_bound,
                    'min_value': df[col].min(),
                    'max_value': df[col].max(),
                    'min_outlier': df[col][outliers_mask].min(),
                    'max_outlier': df[col][outliers_mask].max()
                }
                
                print(f"📈 {col}: {outliers_count} выбросов ({outliers_count/len(df)*100:.1f}%)")
                print(f"   Границы IQR: [{lower_bound:.2f}, {upper_bound:.2f}]")
                print(f"   Фактический диапазон: [{df[col].min():.2f}, {df[col].max():.2f}]")
    
    if not outliers_info:
        print("✅ Выбросы не обнаружены")
        return df
    
    
    # 4. ПРИМЕНЕНИЕ ВЫБРАННОГО МЕТОДА
    print(f"\n🔄 ПРИМЕНЕНИЕ МЕТОДА: {method.upper()}")
    print("-" * 40)
    
    df_cleaned = df.copy()
    removal_results = {}
    
    for col, info in outliers_info.items():
        if method == 'capping':
            # Capping - ограничение выбросов границами IQR
            before_low = (df[col] < info['lower_bound']).sum()
            before_high = (df[col] > info['upper_bound']).sum()
            
            df_cleaned[col] = np.where(df[col] < info['lower_bound'], info['lower_bound'], df[col])
            df_cleaned[col] = np.where(df[col] > info['upper_bound'], info['upper_bound'], df[col])
            
            removed_count = before_low + before_high
            removal_results[col] = {
                'method': 'capping',
                'removed': removed_count,
                'new_range': [df_cleaned[col].min(), df_cleaned[col].max()]
            }
            
            print(f"✅ {col}: ограничено {removed_count} выбросов")
            print(f"   Новый диапазон: [{df_cleaned[col].min():.2f}, {df_cleaned[col].max():.2f}]")
            
        elif method == 'winsorize':
            # Winsorization - ограничение перцентилями
            lower_percentile = df[col].quantile(0.01)
            upper_percentile = df[col].quantile(0.99)
            
            before_low = (df[col] < lower_percentile).sum()
            before_high = (df[col] > upper_percentile).sum()
            
            df_cleaned[col] = np.where(df[col] < lower_percentile, lower_percentile, df[col])
            df_cleaned[col] = np.where(df[col] > upper_percentile, upper_percentile, df[col])
            
            removed_count = before_low + before_high
            removal_results[col] = {
                'method': 'winsorize',
                'removed': removed_count,
                'new_range': [df_cleaned[col].min(), df_cleaned[col].max()],
                'percentiles': [lower_percentile, upper_percentile]
            }
            
            print(f"✅ {col}: winsorized {removed_count} выбросов")
            print(f"   Перцентили [1%, 99%]: [{lower_percentile:.2f}, {upper_percentile:.2f}]")
            
        elif method == 'remove':
            # Удаление строк с выбросами
            outliers_mask = (df[col] < info['lower_bound']) | (df[col] > info['upper_bound'])
            df_cleaned = df_cleaned[~outliers_mask]
            
            removed_count = outliers_mask.sum()
            removal_results[col] = {
                'method': 'remove',
                'removed': removed_count,
                'remaining_rows': len(df_cleaned)
            }
            
            print(f"✅ {col}: удалено {removed_count} строк с выбросами")
            print(f"   Осталось строк: {len(df_cleaned)}")
            
        elif method == 'log':
            # Логарифмическое преобразование (для положительных данных)
            if df[col].min() > 0:
                df_cleaned[col] = np.log1p(df[col])  # log(1 + x) для избежания log(0)
                
                # Пересчитываем выбросы после преобразования
                Q1_new = df_cleaned[col].quantile(0.25)
                Q3_new = df_cleaned[col].quantile(0.75)
                IQR_new = Q3_new - Q1_new
                outliers_new = ((df_cleaned[col] < Q1_new - 1.5 * IQR_new) | 
                               (df_cleaned[col] > Q3_new + 1.5 * IQR_new)).sum()
                
                removal_results[col] = {
                    'method': 'log',
                    'original_outliers': info['before'],
                    'new_outliers': outliers_new,
                    'transformed': True
                }
                
                print(f"✅ {col}: применено логарифмическое преобразование")
                print(f"   Выбросов до: {info['before']}, после: {outliers_new}")
            else:
                print(f"⚠️  {col}: нельзя применить log к неположительным значениям")
                removal_results[col] = {'method': 'skip', 'reason': 'Неположительные значения'}

    return df_cleaned

