import os
from pathlib import Path
import environ


BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(str(BASE_DIR / '.env'))

# 从系统环境变量中读取SECRET_KEY，如果没有则从.env文件中读取
SECRET_KEY = os.environ.get('SECRET_KEY', env('SECRET_KEY'))


# Import the Cloudinary libraries
# ==============================
import cloudinary

# 配置Cloudinary
config = cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME', env('CLOUDINARY_CLOUD_NAME')),
    api_key=os.environ.get('CLOUDINARY_API_KEY', env('CLOUDINARY_API_KEY')),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET', env('CLOUDINARY_API_SECRET')),
    secure=True
)

# Application definition

INSTALLED_APPS = [
    # 'django_crontab',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'whitenoise.runserver_nostatic',
    'corsheaders',
    'courses',
    'memberships',
    'learning_management',
    'dbbackup',  # django-dbbackup
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
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

WSGI_APPLICATION = 'easymath.wsgi.application'

# 添加 CORS 配置
CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:5173', 
#     'https://easymath.vercel.app'
# ]
# CORS_ALLOW_CREDENTIALS = True
 
CORS_ALLOW_METHODS = (
  'DELETE',
  'GET',
  'OPTIONS',
  'PATCH',
  'POST',
  'PUT',
  'VIEW',
)
 
CORS_ALLOW_HEADERS = (
  'XMLHttpRequest',
  'X_FILENAME',
  'accept-encoding',
  'authorization',
  'content-type',
  'dnt',
  'origin',
  'user-agent',
  'x-csrftoken',
  'x-requested-with',
)

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get('PRODUCTION') == 'True':
    DEBUG = False
    ALLOWED_HOSTS = ['web-production-2275.up.railway.app']

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

    # Stripe
    STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY', env('STRIPE_PUBLISHABLE_KEY'))
    STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', env('STRIPE_SECRET_KEY'))

else:
    DEBUG = True
    ALLOWED_HOSTS = []

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

    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': BASE_DIR / 'db.sqlite3',
    #     }
    # }

    # Stripe
    STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_TEST_PUBLISHABLE_KEY', env('STRIPE_TEST_PUBLISHABLE_KEY'))
    STRIPE_SECRET_KEY = os.environ.get('STRIPE_TEST_SECRET_KEY', env('STRIPE_TEST_SECRET_KEY'))


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

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_DIRS = []

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# DBBACKUP
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': BASE_DIR / 'backup'}

# 周期任务
# CRONJOBS = [
#     # 每1分钟备份数据
#     ('*/1 * * * *', 'easymath.cron.backup_data_scheduled_job')
# ]
