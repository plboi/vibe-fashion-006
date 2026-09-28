# VIBE FASHION - 온라인 패션 쇼핑몰 웹앱

Python 3.13 및 Flask 기반의 모던 패션 쇼핑몰 웹 애플리케이션입니다.
초보자도 쉽게 구조를 파악하고 확장할 수 있도록 **애플리케이션 팩토리 패턴(`create_app`)**으로 설계되었습니다.

---

## 📁 프로젝트 폴더 구조

```text
day0/
├── app/
│   ├── __init__.py        # 앱 팩토리 함수 (create_app)
│   ├── routes/            # 페이지 라우트 관리
│   │   ├── __init__.py
│   │   └── main.py        # 홈 및 상품 목록 라우트
│   ├── templates/         # HTML 템플릿 (Jinja2)
│   │   ├── base.html      # 공통 레이아웃 (헤더, 네비, 푸터)
│   │   └── index.html     # 메인 홈 (히어로 섹션, 4개 상품 카드)
│   └── static/            # 정적 자원 (CSS, JS, 이미지 등)
│       └── css/
│           └── style.css  # VIBE FASHION 커스텀 스타일
├── .env.example           # 환경 변수 설정 템플릿
├── .gitignore             # Git 추적 제외 설정
├── requirements.txt       # 의존성 패키지 목록
├── run.py                 # 애플리케이션 실행 진입점
└── README.md              # 프로젝트 안내서
```

---

## 🚀 빠른 시작 가이드

### 1. 가상환경 생성 및 활성화

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화 (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# 가상환경 활성화 (macOS / Linux)
source venv/bin/activate
```

### 2. 패키지 설치

```bash
pip install -r requirements.txt
```

### 3. 환경 변수 파일 생성

```bash
# .env.example 파일을 복사하여 .env 생성
copy .env.example .env   # Windows
# cp .env.example .env   # macOS / Linux
```

### 4. 서버 실행

```bash
python run.py
```

브라우저 주소창에 `http://127.0.0.1:5000` 을 입력하여 접속합니다.

---

## 🛠️ 기술 스택 및 라이브러리

- **Backend**: Python 3.13, Flask 3.x
- **Frontend**: Bootstrap 5.3 CDN, Bootstrap Icons, HTML5, CSS3
- **Dummy Images**: [picsum.photos](https://picsum.photos)
- **Deployment & Config**: Gunicorn, python-dotenv, Supabase Client SDK
