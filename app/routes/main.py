from flask import Blueprint, render_template

# 'main'이라는 이름의 블루프린트 객체 생성
# 블루프린트는 앱의 기능/페이지별로 라우트를 모듈화하여 관리할 수 있게 해줍니다.
main_bp = Blueprint("main", __name__)

# 초보자 학습을 위한 더미 상품 데이터 (4개 상품)
# 실제 프로젝트에서는 Supabase DB나 SQLite 등에서 조회해오는 부분입니다.
# 이미지 URL은 picsum.photos 더미 이미지 서비스를 활용합니다.
DUMMY_PRODUCTS = [
    {
        "id": 1,
        "name": "Classic Overfit Suede Jacket",
        "category": "OUTER",
        "price": 128000,
        "original_price": 160000,
        "discount_rate": 20,
        "badge": "BEST",
        "badge_color": "danger",
        "image_url": "https://images.unsplash.com/photo-1521223890158-f9f7c3d5d504?auto=format&fit=crop&w=800&q=80",
        "description": "실버 대거 메탈 버튼 포인트와 딥 블랙 스웨이드 텍스처가 돋보이는 럭셔리 고딕 자켓입니다.",
        "rating": 4.9,
        "reviews_count": 128
    },
    {
        "id": 2,
        "name": "헤비웨이트 빈티지 워싱 후드",
        "category": "TOP",
        "price": 69000,
        "original_price": 89000,
        "discount_rate": 22,
        "badge": "NEW",
        "badge_color": "primary",
        "image_url": "https://picsum.photos/id/824/600/750",
        "description": "탄탄한 코튼 100% 원단과 트렌디한 피그먼트 워싱으로 완성된 후드 티셔츠입니다.",
        "rating": 4.8,
        "reviews_count": 86
    },
    {
        "id": 3,
        "name": "와이드 스트레이트 워싱 데님",
        "category": "BOTTOM",
        "price": 54000,
        "original_price": 54000,
        "discount_rate": 0,
        "badge": "MD PICK",
        "badge_color": "success",
        "image_url": "https://picsum.photos/id/646/600/750",
        "description": "체형을 커버해주는 완벽한 와이드 핏과 자연스러운 브러쉬 워싱 팬츠입니다.",
        "rating": 4.7,
        "reviews_count": 215
    },
    {
        "id": 4,
        "name": "미니멀 레더 코트 스니커즈",
        "category": "SHOES",
        "price": 89000,
        "original_price": 119000,
        "discount_rate": 25,
        "badge": "SALE",
        "badge_color": "warning",
        "image_url": "https://picsum.photos/id/103/600/750",
        "description": "어떤 코디에도 자연스럽게 어울리는 심플하고 모던한 실루엣의 스니커즈입니다.",
        "rating": 4.9,
        "reviews_count": 94
    }
]


@main_bp.route("/")
def index():
    """
    홈 화면 라우트 함수
    - 더미 상품 데이터를 index.html 템플릿에 전달하여 화면에 렌더링합니다.
    """
    return render_template("index.html", products=DUMMY_PRODUCTS)
