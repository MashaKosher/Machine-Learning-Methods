import pandas as pd


def one_hot_encode(df: pd.DataFrame, columns: list[str] | None = None, drop_first: bool = False) -> pd.DataFrame:
    """
    Применяет One-Hot Encoding к указанным категориальным столбцам.
    Если columns=None, автоматически выберет object/categorical столбцы.
    """
    data = df.copy()
    if columns is None:
        columns = data.select_dtypes(include=['object', 'category']).columns.tolist()
    if not columns:
        return data
    encoded = pd.get_dummies(data, columns=columns, drop_first=drop_first, dtype='int8')
    return encoded


def binarize_columns(
    df: pd.DataFrame,
    spec: dict[str, float] | None = None,
    columns: list[str] | None = None,
) -> pd.DataFrame:
    """
    Бинаризация числовых столбцов по порогу.
    spec: словарь {column: threshold}. Если spec=None, бинаризуем по медиане автоматически.
    columns: список столбцов-кандидатов. По умолчанию берём подходящие числовые.
    """
    data = df.copy()
    # Определяем кандидатов: числовые, не оканчиваются на _bin, не one-hot (не строго 0/1), не константные
    if columns is None:
        candidates = []
        for col in data.select_dtypes(include=['number']).columns:
            if col.endswith('_bin'):
                continue
            # Пропустим явные OHE-добивки (только 0/1)
            unique_vals = data[col].dropna().unique()
            if len(unique_vals) <= 2 and set(unique_vals).issubset({0, 1}):
                continue
            # Пропустим константные
            if data[col].nunique(dropna=True) <= 1:
                continue
            candidates.append(col)
    else:
        candidates = [c for c in columns if c in data.columns]

    if spec is None:
        spec = {}
        for col in candidates:
            try:
                med = data[col].median()
                if pd.isna(med):
                    continue
                spec[col] = float(med)
            except Exception:
                continue

    new_cols: dict[str, pd.Series] = {}
    for col, thr in spec.items():
        if col in data.columns and pd.api.types.is_numeric_dtype(data[col]):
            # Защита от полностью NaN
            series = data[col]
            if series.notna().sum() == 0:
                continue
            new_cols[f'{col}_bin'] = (series > thr).astype('int8')

    if new_cols:
        bin_df = pd.DataFrame(new_cols, index=data.index)
        data = pd.concat([data, bin_df], axis=1)
        # дефрагментация
        data = data.copy()

    return data


