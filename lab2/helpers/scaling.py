import pandas as pd


def standardize(df: pd.DataFrame, columns: list[str] | None = None) -> pd.DataFrame:
    """
    Стандартизация (Z-score): (x - mean) / std
    По умолчанию применяет ко всем числовым столбцам.
    Возвращает копию с суффиксом _std для преобразованных столбцов.
    """
    data = df.copy()
    if columns is None:
        columns = data.select_dtypes(include=['number']).columns.tolist()
    new_cols: dict[str, pd.Series] = {}
    for col in columns:
        if col in data.columns:
            mean = data[col].mean()
            std = data[col].std()
            if std == 0 or pd.isna(std):
                new_cols[f'{col}_std'] = pd.Series(0.0, index=data.index)
            else:
                new_cols[f'{col}_std'] = (data[col] - mean) / std
    if new_cols:
        std_df = pd.DataFrame(new_cols, index=data.index)
        data = pd.concat([data, std_df], axis=1)
        data = data.copy()
    return data


def minmax_scale(df: pd.DataFrame, columns: list[str] | None = None, feature_range: tuple[float, float] = (0.0, 1.0)) -> pd.DataFrame:
    """
    Нормализация Min-Max: (x - min) / (max - min) в заданный диапазон.
    По умолчанию ко всем числовым колонкам. Создает столбцы с суффиксом _mm.
    """
    data = df.copy()
    if columns is None:
        columns = data.select_dtypes(include=['number']).columns.tolist()
    min_r, max_r = feature_range
    new_cols: dict[str, pd.Series] = {}
    for col in columns:
        if col in data.columns:
            col_min = data[col].min()
            col_max = data[col].max()
            denom = col_max - col_min
            if denom == 0 or pd.isna(denom):
                new_cols[f'{col}_mm'] = pd.Series(min_r, index=data.index)
            else:
                scaled = (data[col] - col_min) / denom
                new_cols[f'{col}_mm'] = scaled * (max_r - min_r) + min_r
    if new_cols:
        mm_df = pd.DataFrame(new_cols, index=data.index)
        data = pd.concat([data, mm_df], axis=1)
        data = data.copy()
    return data


