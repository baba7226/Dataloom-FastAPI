from app.models.schemas import CleanResponse, CleanRequest, CleanedItem

def clean_data(request: CleanRequest) -> CleanResponse:
    """
        业务层函数：执行最简单的清洗逻辑
        - 去掉每个值前后的空格
        - 如果为空，则返回None
    """
    result = []

    # 遍历输入的每一行数据
    for item in request.data:
        cleaned_value = item.value.strip() if item.value else None
        result.append(CleanedItem(column=item.column, cleaned_value=cleaned_value))
        return CleanResponse(status=200, data=result)