# Intern_Assignment



assignment/
│
├── config/                  # 프로젝트 설정
│   ├── __init__.py
│   ├── settings.py         # 프로젝트 설정 파일
│   ├── urls.py            # 메인 URL 설정
│   ├── wsgi.py
│   └── asgi.py
│
├── accounts/               # 계정 관리 앱
│   ├── __init__.py
│   ├── models.py          # User 모델
│   ├── views.py           # 회원가입/로그인 뷰
│   ├── urls.py           # 계정 관련 URL
│   └── serializers.py     # 시리얼라이저
│
├── utils/                  # 유틸리티 앱
│   ├── __init__.py
│   ├── permissions.py     # 권한 관련 유틸
│   └── tests/             # 테스트 코드
│       ├── __init__.py
│       ├── conftest.py    # pytest 설정
│       ├── test_auth.py   # 인증 테스트
│       └── test_roles.py  # 역할 테스트
│
├── .env                   # 환경 변수 (git에서 제외)
├── .env.example          # 환경 변수 예시
├── .gitignore           # git 제외 파일 목록
├── requirements.txt     # 패키지 의존성
├── manage.py           # Django 관리 스크립트
└── pytest.ini         # pytest 설정 파일