from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/lectures/{lecture_id}/details")
def get_lecture_details(lecture_id: str):
    example_data = {
        "12345": {
            "id": "12345",
            "schedule": [
                {"day": "월", "time": "10:00-11:30"},
                {"day": "수", "time": "10:00-11:30"}
            ],
            "classroom": "3550"
        }
    }

    if lecture_id not in example_data:
        raise HTTPException(status_code=400, detail="Invalid lecture ID")

    return example_data[lecture_id]