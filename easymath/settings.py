import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

import environ
env = environ.Env()
env.read_env(str(BASE_DIR / '.env'))

# 从系统环境变量中读取SECRET_KEY，如果没有则从.env文件中读取
SECRET_KEY = os.environ.get('SECRET_KEY', env('SECRET_KEY'))


# Import the Cloudinary libraries
# ==============================
import cloudinary
# import cloudinary.uploader
# import cloudinary.api

# 配置Cloudinary
config = cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME', env('CLOUDINARY_CLOUD_NAME')),
    api_key=os.environ.get('CLOUDINARY_API_KEY', env('CLOUDINARY_API_KEY')),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET', env('CLOUDINARY_API_SECRET')),
    secure=True
)


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

if not DEBUG:
    CSRF_TRUSTED_ORIGINS = ['https://web-production-2dfb.up.railway.app']

# Application definition

INSTALLED_APPS = [
    'django_crontab',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'courses',
    'memberships',
    'learning_management',
    'rest_framework',
    'dbbackup',  # django-dbbackup
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

ROOT_URLCONF = 'easymath.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'easymath.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('PGDATABASE', env('PGDATABASE')),
        'USER': os.environ.get('PGUSER', env('PGUSER')),
        'PASSWORD': os.environ.get('PGPASSWORD', env('PGPASSWORD')),
        'HOST': os.environ.get('PGHOST', env('PGHOST')),
        'PORT': os.environ.get('PGPORT', env('PGPORT')),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'staticfiles/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Stripe
if DEBUG:
    STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_TEST_PUBLISHABLE_KEY', env('STRIPE_TEST_PUBLISHABLE_KEY'))
    STRIPE_SECRET_KEY = os.environ.get('STRIPE_TEST_SECRET_KEY', env('STRIPE_TEST_SECRET_KEY'))
else:
    # live keys
    STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY', env('STRIPE_PUBLISHABLE_KEY'))
    STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', env('STRIPE_SECRET_KEY'))

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': BASE_DIR / 'backup'}

# 周期任务
CRONJOBS = [
    # 每1分钟备份数据
    ('*/1 * * * *', 'easymath.cron.backup_data_scheduled_job')
]