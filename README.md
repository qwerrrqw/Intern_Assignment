# Intern_Assignment

## 프로젝트 구조
```bash
assignment/
├── config/                  # 프로젝트 설정
├── accounts/               # 계정 관리 앱
├── utils/                  # 유틸리티 앱
├── .env                   # 환경 변수(설치방법 4번 항목 참조)
├── .gitignore            # git 제외 파일
├── requirements.txt      # 의존성 패키지
└── manage.py            # Django 관리 스크립트
```

## 기술 스택
- Python 3.11
- Django 5.1
- Django REST Framework
- Simple JWT
- drf-yasg (Swagger/OpenAPI)

## 주요 기능
- JWT 기반 사용자 인증 시스템
- 회원가입/로그인 API
- 사용자 역할(Role) 관리
- Swagger UI API 문서화

## 설치 방법

### 1. 레포지토리 클론
```bash
git clone https://github.com/qwerrrqw/Intern_Assignment.git
cd assignment
```

### 2. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. 환경 변수 설정
```bash
DJANGO_ENV=development
SECRET_KEY=your-secret-key
```

### 5. 데이터베이스 마이그레이션
```bash
python manage.py migrate
```

### 6. 개발 서버에서 실행
```bash
python manage.py runserver
```

### 7. API 엔드포인트
- Swagger UI: `http://3.34.186.143/swagger/`
- ReDoc: `http://3.34.186.143/redoc/`
- 회원가입: `POST http://3.34.186.143/api/accounts/signup/`
- 로그인: `POST http://3.34.186.143/api/accounts/login/`



## 테스트
```bash
pytest
```

## 라이선스
```bash
BSD License
```