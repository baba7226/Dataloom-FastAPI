import pandas as pd
from app.models.schemas import ColumnAnalysis

def analyze_dataframe(df: pd.DataFrame) -> list[ColumnAnalysis]:
    analysis = []

    for col in df.columns:
        dtype = str(df[col].dtype)
        missing_rate = df[col].isnull().mean()
        unique_count = df[col].nunique()
        is_date = False

        # Try to infer date
        try:
            pd.to_datetime(df[col])
            is_date = True
        except:
            pass

        analysis.append(ColumnAnalysis(
            column=col,
            dtype=dtype,
            missing_rate=round(missing_rate, 4),
            unique_count=int(unique_count),
            is_date=is_date
        ))

    return analysis
