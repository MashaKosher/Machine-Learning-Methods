import pandas as pd

def get_columns_with_misses(df: pd.DataFrame) -> list:
    return df.columns[df.isnull().any()].tolist()


def get_numeric_columns(df: pd.DataFrame) -> list:
    return df.select_dtypes(include=['number']).columns.tolist()[1:] # first element is user id we don't need to analyze it 

def get_anomal_columns(df: pd.DataFrame, columns_to_analyze: list[str]) -> list:
    columnToFix = []
    for col in columns_to_analyze:
        
        # Рассчитываем статистику для выбросов
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)][col]
        outliers_percentage = len(outliers) / len(df) * 100

        if outliers_percentage > 0.0001:
            print(col, outliers_percentage)
            columnToFix.append(col)

    return columnToFix
    
