import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '자신의 키를 입력하세요'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # 실제 호스트를 추가해야 합니다.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djongo',
    'Jpage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CSRF_COOKIE_NAME = 'csrftoken'  # CSRF 쿠키 이름 설정
CSRF_COOKIE_SECURE = True       # HTTPS에서만 쿠키 전송
CSRF_COOKIE_HTTPONLY = True     # JavaScript에서 접근 불가
CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'  # CSRF 토큰을 포함할 헤더 이름

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'common_templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'common.context_processors.get_user'
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'MyDiary',  # 사용할 MongoDB 데이터베이스 이름
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb://192.168.0.25:27017/',  # MongoDB 호스트 주소 (기본적으로는 localhost)
        }
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'diaryData',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'mongodb://localhost:27017/',
            'username': '자신의 키를 입력하세요',
            'password': '자신의 키를 입력하세요',
            'authMechanism': 'SCRAM-SHA-1',  # MongoDB 클라우드에 맞는 인증 메커니즘 설정
        }
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

STATIC_URL = '/static/'  # 정적 파일 URL 끝에 슬래시 추가
STATICFILES_DIRS = [
    BASE_DIR /'static/'
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

X_FRAME_OPTIONS = 'SAMEORIGIN'
