"""
VIBE FASHION 실행 진입점 (Entry Point)
=====================================
이 파일을 직접 실행하거나, gunicorn / flask run 명령어의 시작점으로 사용합니다.
- 로컬 실행: python run.py
- 프로덕션 배포(Linux): gunicorn "run:app"
"""

from app import create_app

# 애플리케이션 팩토리 함수를 호출하여 Flask 앱 인스턴스 생성
app = create_app()

if __name__ == "__main__":
    # 개발 서버 실행 (코드 변경 시 자동 재시작: debug=True)
    # 기본 포트 5000번으로 실행됩니다. (http://127.0.0.1:5000)
    print("=" * 60)
    print(" [VIBE FASHION] 패션 쇼핑몰 서버가 시작되었습니다.")
    print(" 브라우저에서 http://127.0.0.1:5000 접속하여 확인하세요.")
    print("=" * 60)
    app.run(host="127.0.0.1", port=5000, debug=True)
