from fastapi import FastAPI, Query, HTTPException
from typing import Optional

app = FastAPI()

@app.get("/lectures")
def search_lectures(
    field: str = Query(..., description="lecture 또는 professor"),
    keyword: str = Query(..., description="검색 키워드"),
    offset: int = Query(0, description="페이지 오프셋 값")
):
    if field not in ["lecture", "professor"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid value for 'field'. Must be 'lecture' or 'professor'."
        )

    example_data = [
        {"id": "12345", "name": "데이터베이스", "professor": "김철수", "rate": 3.0, "schedule": "월/수 10:00-11:30"},
        {"id": "67890", "name": "운영체제", "professor": "이영희", "rate": 4.2, "schedule": "화/목 09:00-10:30"},
    ]

    filtered = [
        lec for lec in example_data
        if (keyword in lec["name"] if field == "lecture" else keyword in lec["professor"])
    ]

    return {
        "lectures": filtered[offset:offset + 10],
        "next_offset": offset + 10,
        "total": len(filtered)
    }