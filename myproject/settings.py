"""
Django settings for myproject myproject.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from decouple import config
import os

from dotenv import load_dotenv


# Build paths inside the myproject like this: BASE_DIR / 'subdir'.
# Build paths inside the myproject like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# .env 파일 경로 설정
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# # Open api key
# OPENAI_API_KEY = config('OPENAI_API_KEY')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-a&)gx3mp+#9epz5&okvg@x6e*a#z%9%#p(k_uwl7w%bkwcntve"
OPEN_API_KEY = os.getenv('OPEN_API_KEY')
DEBUG = 'True'
# SECURITY WARNING: don't run with debug turned on in production!

# ALLOWED_HOSTS = []
# settings.py
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "diaryapp",
    "taggit.apps.TaggitAppConfig",
    'django.contrib.humanize',
]
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

ROOT_URLCONF = "myproject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
                    os.path.join(BASE_DIR, 'common_templates'),
                ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "myproject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'diary',  # 사용할 MongoDB 데이터베이스 이름
#         'ENFORCE_SCHEMA': False,
#         'CLIENT': {
#             'host': 'mongodb://localhost',  # MongoDB 호스트 주소 (기본적으로는 localhost)
#             'port': 27017,  # MongoDB 포트 (기본적으로는 27017)
#         }
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'MyDiary',  # 사용할 MongoDB 데이터베이스 이름
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': os.getenv('DB_HOST'),  # MongoDB 호스트 주소 (기본적으로는 localhost)
            'username': os.getenv('DB_USERNAME'),
            'password': os.getenv('DB_PASSWORD'),
        }
    }
}


# 미디어 파일 저장 경로
MEDIA_URL = '/media/'
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 이미지 DB
MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DB_NAME = 'diary'
MEDIA_BASE_URL = 'http://localhost:8000/media/'  # GridFS의 파일을 접근할 수 있는 기본 URL


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


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# DEFAULT_FROM_EMAIL = "new@gmail.com"
DEFAULT_FROM_EMAIL = "neweeee@gmail.com"
# DEFAULT_FROM_EMAIL = "fx567849@gmail.com"