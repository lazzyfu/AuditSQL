"""
Django settings for yasql project.

Generated by 'django-admin startproject' using Django 2.2.15.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import datetime
import logging.config
import os
import sys

from kombu import Queue

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from config import REDIS, DB, LDAP_SUPPORT, NOTICE, DEBUG_ENABLED

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define apps path
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# define user auth model
AUTH_USER_MODEL = 'users.UserAccounts'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm3cfrcrlbikc16h+u8c4!gru$h8@4k)@m^p4$f=bwqi1o$r_c^'

# SECURITY WARNING: don't run with debug turned on in production!
if DEBUG_ENABLED:
    DEBUG = True
    ALLOWED_HOSTS = []
else:
    DEBUG = False
    ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_celery_results',
    'django_celery_beat',
    'channels',
    'users',
    'sqlorders',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

JWT_AUTH = {
    # 设置token过期时间为12小时
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=12 * 60 * 60),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_ALLOW_REFRESH': True,
    'JWT_SECRET_KEY': None,
    'JWT_GET_USER_SECRET_KEY': 'users.utils.jwt_get_user_secret',  # 为每个用户动态生成加密key
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=1),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'yasql.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'yasql.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB['database'],
        'USER': DB['user'],
        'HOST': DB['host'],
        'PORT': DB['port'],
        'PASSWORD': DB['password'],
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        }
    }
}

# Redis For Session
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://:{REDIS['password']}@{REDIS['host']}:{REDIS['port']}/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# 静态文件
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# media文件
MEDIA_URL = '/api/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Celery Config
CELERY_BROKER_URL = f"redis://:{REDIS['password']}@{REDIS['host']}:{REDIS['port']}/0"
CELERY_RESULT_BACKEND = f"redis://:{REDIS['password']}@{REDIS['host']}:{REDIS['port']}/0"
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_TASK_DEFAULT_QUEUE = 'default'
CELERY_TASK_DEFAULT_EXCHANGE_TYPE = 'topic'
CELERY_TASK_DEFAULT_ROUTING_KEY = 'default'

CELERY_TASK_QUEUES = (
    Queue('default', routing_key='default'),  # 默认队列
    Queue('dbtask', routing_key='dbtask'),  # 数据库工单任务
)

CELERY_TASK_ROUTES = {
}

CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_WORKER_MAX_TASKS_PER_CHILD = 40
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# django-channels
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [f"redis://:{REDIS['password']}@{REDIS['host']}:{REDIS['port']}/0", ],
            "capacity": 1500,  # default 100
            "expiry": 10,  # default 60
        },
    },
}

ASGI_APPLICATION = "yasql.routing.application"

# 启用LDAP支持
if LDAP_SUPPORT['enable'] is True:
    AUTHENTICATION_BACKENDS = [
        'django_auth_ldap.backend.LDAPBackend',
        'django.contrib.auth.backends.ModelBackend',
    ]

    AUTH_LDAP_SERVER_URI = LDAP_SUPPORT['config']['AUTH_LDAP_SERVER_URI']
    AUTH_LDAP_ALWAYS_UPDATE_USER = LDAP_SUPPORT['config']['AUTH_LDAP_ALWAYS_UPDATE_USER']
    AUTH_LDAP_BIND_DN = LDAP_SUPPORT['config']['AUTH_LDAP_BIND_DN']
    AUTH_LDAP_BIND_PASSWORD = LDAP_SUPPORT['config']['AUTH_LDAP_BIND_PASSWORD']
    AUTH_LDAP_USER_SEARCH = LDAP_SUPPORT['config']['AUTH_LDAP_USER_SEARCH']
    AUTH_LDAP_USER_ATTR_MAP = LDAP_SUPPORT['config']['AUTH_LDAP_USER_ATTR_MAP']

# 邮箱配置
if NOTICE['MAIL']['enabled'] is True:
    EMAIL_HOST = NOTICE['MAIL']['email_host']
    EMAIL_PORT = NOTICE['MAIL']['email_port']
    EMAIL_HOST_USER = NOTICE['MAIL']['email_host_user']
    EMAIL_HOST_PASSWORD = NOTICE['MAIL']['email_host_password']
    EMAIL_FROM = NOTICE['MAIL']['email_host_user']
    EMAIL_USE_SSL = NOTICE['MAIL']['email_use_ssl']

# logging
logging.config.fileConfig(os.path.join(BASE_DIR, 'logging.ini'), disable_existing_loggers=False)
