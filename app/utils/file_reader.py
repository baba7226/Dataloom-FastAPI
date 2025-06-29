import pandas as pd
import io
from fastapi import UploadFile, HTTPException
import chardet

async def read_csv_to_df(file: UploadFile) -> pd.DataFrame:
    content = await file.read()
    encoding = chardet.detect(content)['encoding'] or 'utf-8'
    try:
        df = pd.read_csv(io.StringIO(content.decode(encoding)))
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error reading CSV with detected encoding {encoding}: {e}"
        )
    return df
