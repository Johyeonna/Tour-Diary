"""
Django settings for myproject

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import pymongo
import os
from dotenv import load_dotenv
import json
from datetime import timedelta
import sys
import urllib.parse

from pymongo import MongoClient

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_BASE_DIR = Path(__file__).resolve().parent

# .env 파일 경로 설정
env_path = BASE_DIR / '.env'
load_dotenv(dotenv_path=env_path)

SECRET_BASE_FILE = os.path.join(CONFIG_BASE_DIR, 'secrets/secrets.json')
secrets = json.loads(open(SECRET_BASE_FILE).read())

secrets['SECRET_KEY'] = os.getenv('SECRET_KEY')
secrets['NAVER_CLIENT_ID'] = os.getenv('NAVER_CLIENT_ID')
secrets['NAVER_REDIRECT_URI'] = "http://localhost:8000/oauth/naver/login/callback/"
secrets['NAVER_CLIENT_SECRET'] = os.getenv('NAVER_CLIENT_SECRET')
secrets['STATE'] = os.getenv('STATE')

with open(SECRET_BASE_FILE, 'w') as f:
    json.dump(secrets, f, indent=4)
for key, value in secrets.items():
    setattr(sys.modules[__name__], key, value)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-a&)gx3mp+#9epz5&okvg@x6e*a#z%9%#p(k_uwl7w%bkwcntve"
OPEN_API_KEY = os.getenv('OPEN_API_KEY')
# DEBUG 설정
DEBUG = True

# ALLOWED_HOSTS 설정
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "travel_recommend",
    "diaryapp",
    'Jpage',
    "taggit.apps.TaggitAppConfig",
    'django.contrib.humanize',
    # external library
    'rest_framework',
    # 'rest_framework_simplejwt.token_blacklist',
    'drf_yasg',
    'oauth',
    'users'
]

SITE_ID = 1

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [  # 기본 Permission 설정
        # 'rest_framework.permissions.AllowAny',  # 모든 계정 액세스 허용
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (  # Authenticationt 설정
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': [  # api 결과 전달 방식
        'rest_framework.renderers.JSONRenderer',  # json 방식
    ],
    'DEFAULT_PARSER_CLASSES': [  # 요청 받을 때 body 형태
        'rest_framework.parsers.JSONParser',
        # 'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',  # serializer datetime format
}

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_PASSWORD_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'

REST_USE_JWT = False
ACCOUNT_LOGOUT_ON_GET = False
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=24),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=14),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS512',
    'SIGNING_KEY': '',

    'AUTH_HEADER_TYPES': ('Bearer',),  # 인증 헤더 유형
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',  # 인증 헤더 명칭
    'USER_ID_FIELD': 'email',  # 사용자 식별을 위한 토큰에 포함할 사용자 모델의 DB 필드명
    'USER_ID_CLAIM': 'email',  # 사용자 식별을 저장하는 데 사용할 생성된 토큰의 클레임

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),  # 토큰 유형 지정 클래스
    'TOKEN_TYPE_CLAIM': 'token_type',  # 토큰 유형 저장 클레임 명칭

    'JTI_CLAIM': 'jti',
}

AUTH_USER_MODEL = 'users.UserModel'
AUTHENTICATION_BACKENDS = (
    'users.lib.backends.SettingsBackend',
    'django.contrib.auth.backends.ModelBackend',
)

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },

    'LOGIN_URL': 'users:login',
    'LOGOUT_URL': 'users:logout',
    'USE_SESSION_AUTH': False,
}

TAGGIT_CASE_INSENSITIVE = True
TAGGIT_LIMIT = 50

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
CSRF_COOKIE_HTTPONLY = True
ROOT_URLCONF = "myproject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, 'common_templates')
            # os.path.join(BASE_DIR, 'users', 'templates')
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "common.context_processors.main_badge",
                "common.context_processors.get_user",
            ],
        },
    },
]

# SECRET_KEY = '자신의 키를 입력하세요'

CSRF_COOKIE_NAME = 'csrftoken'  # CSRF 쿠키 이름 설정
CSRF_COOKIE_SECURE = True       # HTTPS에서만 쿠키 전송
CSRF_COOKIE_HTTPONLY = True     # JavaScript에서 접근 불가
CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'  # CSRF 토큰을 포함할 헤더 이름

WSGI_APPLICATION = "myproject.wsgi.application"

# MongoDB 설정
MONGO_URI = 'mongodb://127.0.0.1:27017/'
#MONGO_URI = os.getenv('ATLAS_URI')


# # MongoDB 설정
# MONGO_URI = 'mongodb://192.168.0.25:27017/'

# MongoDB 도커
# MongoDB 도커
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'MyDiary',  # 사용할 MongoDB 데이터베이스 이름
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            #'host': 'mongodb://127.0.0.1:27017/',  # MongoDB 호스트 주소 (기본적으로는 localhost)
            'host': 'mongodb://127.0.0.1:27017/',
        }
    }
}
# MongoDB 클라이언트 설정
mongo_client = pymongo.MongoClient(DATABASES['default']['CLIENT']['host'],
                                   )
# mongo_client를 settings에 추가
MONGO_CLIENT = mongo_client





# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
    ]


X_FRAME_OPTIONS = 'SAMEORIGIN'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DEFAULT_FROM_EMAIL = "neweeee@gmail.com"

