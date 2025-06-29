from fastapi import APIRouter, UploadFile, HTTPException
from app.utils.file_reader import read_csv_to_df
from app.services import analyzer, recommender
from app.models.schemas import RecommendationResult

router = APIRouter()

@router.post("/recommend", response_model=RecommendationResult)
async def recommend_cleaning(file: UploadFile):
    try:
        df = await read_csv_to_df(file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading CSV: {e}")

    analysis = analyzer.analyze_dataframe(df)
    recommendations = recommender.generate_recommendations(analysis)

    return RecommendationResult(
        analysis=analysis,
        recommendations=recommendations
    )
