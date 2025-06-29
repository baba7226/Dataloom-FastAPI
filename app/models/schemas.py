from typing import List, Optional
from pydantic import BaseModel

# 单个输入数据项的结构
class DataItem(BaseModel):
    column: str
    value: Optional[str]

# ( POST   /clean )请求体的结构
class CleanRequest(BaseModel):
    data: List[DataItem]

# 单个输出结果项
class CleanedItem(BaseModel):
    column: str
    cleaned_value: Optional[str]

# 接口返回的响应体结构
class CleanResponse(BaseModel):
    column: str
    clean_value: Optional[str]

class ColumnAnalysis(BaseModel):
    column: str
    dtype: str
    missing_rate: float
    unique_count: int
    is_date: bool

class ColumnRecommendation(BaseModel):
    column: str
    recommendations: List[str]

class RecommendationResult(BaseModel):
    analysis: List[ColumnAnalysis]
    recommendations: List[ColumnRecommendation]
