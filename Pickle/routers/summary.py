from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/lectures/{lecture_id}/summary")
def get_lecture_summary(lecture_id: str):
    example_data = {
        "12345": {
            "id": "12345",
            "name": "데이터베이스",
            "professor": "김철수",
            "rate": 3.0,
            "review_count": 25,
            "cards": [
                {
                    "type": "STYLE",
                    "content": ["강의가 체계적이다.", "시험 난이도가 중간 수준이다."]
                },
                {
                    "type": "TEST",
                    "content": ["기말고사만 진행", "PPT에서 지엽적인 내용까지 나왔음"]
                },
                {
                    "type": "ASSIGNMENT",
                    "content": ["과제가 많음", "팀플이 있음"]
                },
                {
                    "type": "RECOMMEND",
                    "content": ["교수님 강의력 좋아요", "과제 많지만 어렵지 않음"]
                },
                {
                    "type": "NON_RECOMMEND",
                    "content": ["프로젝트 난이도 높고 SQL 기초 지식 필요", "과제 많은 편"]
                },
                {
                    "type": "TIP",
                    "content": ["프로젝트 팀원 중요하다", "실습 때 열심히 참여하는 모습 보이면 점수 잘 준다"]
                }
            ]
        }
    }

    if lecture_id not in example_data:
        raise HTTPException(status_code=400, detail="Invalid lecture ID")

    return example_data[lecture_id]