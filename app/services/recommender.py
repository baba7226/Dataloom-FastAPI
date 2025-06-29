from app.models.schemas import ColumnAnalysis, ColumnRecommendation

def generate_recommendations(analysis: list[ColumnAnalysis]) -> list[ColumnRecommendation]:
    recommendations = []

    for col in analysis:
        recs = []

        if col.missing_rate > 0.3:
            recs.append("建议删除（缺失率高）")
        elif col.missing_rate > 0:
            recs.append("建议填充（均值/中位数/众数）")

        if col.dtype == 'object' and col.unique_count < 10:
            recs.append("建议做编码（One-Hot / Label）")

        if col.is_date:
            recs.append("建议转换为日期时间格式")

        recommendations.append(ColumnRecommendation(
            column=col.column,
            recommendations=recs
        ))

    return recommendations
