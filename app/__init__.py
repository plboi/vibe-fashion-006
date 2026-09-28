import os
from flask import Flask
from dotenv import load_dotenv

# .env 파일이 존재하는 경우 환경 변수를 자동으로 불러옵니다.
load_dotenv()


def create_app(test_config=None):
    """
    [애플리케이션 팩토리 패턴 (Application Factory Pattern)]
    Flask 앱 인스턴스를 함수 내부에서 생성하고 구성하여 반환합니다.
    이 패턴을 사용하면 다음과 같은 장점이 있습니다:
    1. 여러 설정(개발, 테스트, 배포)으로 앱을 쉽게 생성할 수 있습니다.
    2. 순환 참조(Circular Import) 문제를 방지할 수 있습니다.
    3. 단위 테스트 작성 시 독립된 앱 환경을 만들기 쉽습니다.
    """
    # Flask 애플리케이션 인스턴스 생성
    # instance_relative_config=True 로 설정하여 instance 폴더 기준 설정 파일을 불러올 수 있도록 합니다.
    app = Flask(__name__, instance_relative_config=True)

    # 기본 설정 값 지정
    app.config.from_mapping(
        # 세션 및 폼 보안을 위한 비밀키 (실제 배포 시에는 .env의 SECRET_KEY를 권장)
        SECRET_KEY=os.getenv("SECRET_KEY", "dev-secret-key-default"),
        # Supabase 연동 정보 (추후 DB 연결 시 사용)
        SUPABASE_URL=os.getenv("SUPABASE_URL", ""),
        SUPABASE_KEY=os.getenv("SUPABASE_KEY", ""),
    )

    if test_config is not None:
        # 테스트 환경 설정이 전달된 경우 덮어씌웁니다.
        app.config.from_mapping(test_config)

    # 블루프린트(Blueprint) 등록
    # routes/main.py 에 정의된 메인 라우트를 앱에 연결합니다.
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    return app
