import pandas as pd
import numpy as np


def generate_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Генерирует новые признаки на основе имеющихся колонок.

    Добавляем как минимум два признака:
    - Num_Product_Categories: сколько категорий товара указано у записи (1..3)
    - Has_Prod_Cat_3: бинарный индикатор наличия Product_Category_3
    - Purchase_per_Category: средняя сумма покупки на категорию (если есть Purchase)
    - Is_High_Spender: бинарный индикатор больших трат (квантиль 0.75)

    Функция устойчиво работает, даже если каких-то колонок нет в датасете.
    """
    data = df.copy()

    prod_cols = [c for c in [
        'Product_Category_1', 'Product_Category_2', 'Product_Category_3'
    ] if c in data.columns]

    if len(prod_cols) > 0:
        # Сколько непустых категорий товара указано
        data['Num_Product_Categories'] = data[prod_cols].notna().sum(axis=1).astype('int16')
    else:
        data['Num_Product_Categories'] = 0

    if 'Product_Category_3' in data.columns:
        data['Has_Prod_Cat_3'] = data['Product_Category_3'].notna().astype('int8')
    else:
        data['Has_Prod_Cat_3'] = 0

    # Покупка на категорию (если есть колонка Purchase)
    if 'Purchase' in data.columns:
        denom = data['Num_Product_Categories'].replace(0, np.nan)
        data['Purchase_per_Category'] = (data['Purchase'] / denom).fillna(0)

        # Индикатор большого чека по верхнему квартилю
        try:
            threshold = data['Purchase'].quantile(0.75)
            data['Is_High_Spender'] = (data['Purchase'] > threshold).astype('int8')
        except Exception:
            data['Is_High_Spender'] = 0
    else:
        data['Purchase_per_Category'] = 0.0
        data['Is_High_Spender'] = 0

    return data


