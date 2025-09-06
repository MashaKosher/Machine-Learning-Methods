from pathlib import Path
from typing import Optional
import pandas as pd


def load_data(file_path: str, **kwargs) -> Optional[pd.DataFrame]:
    """
    Загрузка данных с обработкой ошибок
    
    Args:
        file_path: путь к файлу
        **kwargs: дополнительные параметры для pd.read_csv
        
    Returns:
        DataFrame или None в случае ошибки
    """
    try:
        path = Path(file_path)
        if not path.exists():
            print(f"Файл {file_path} не найден")
            return None
        
        print(f"Загрузка данных из {file_path}")
        df = pd.read_csv(file_path, **kwargs)
        print(f"Данные успешно загружены. Форма: {df.shape}")
        return df
        
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")
        return None
