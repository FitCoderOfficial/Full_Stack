from pathlib import Path
from datetime import timedelta
import environ
import sys
import dj_database_url
import django_heroku

# Activate Django-Heroku.
django_heroku.settings(locals())

env = environ.Env(
    DEBUG=(bool, True)
)

READ_DOT_ENV_FILE = env.bool('READ_DOT_ENV_FILE', default=True)
if READ_DOT_ENV_FILE:
    environ.Env.read_env()


DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEVELOPMENT_MODE = env('DEVELOPMENT_MODE')

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com', "*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",

    # installed apps
    "rest_framework",
    'rest_framework.authtoken',
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    
    'dj_rest_auth',
    'dj_rest_auth.registration',

    'djoser',
    'storages',


    'social_django',

    'corsheaders',
    "drf_yasg",

    # local apps
    "apps.user", 
    "apps.post",
    "apps.comment",
    

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # whitenoise
    "whitenoise.middleware.WhiteNoiseMiddleware",
    
    # corsheaders
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [ BASE_DIR / "templates"],
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

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'FullAuth_API',
        'USER': 'master',
        'PASSWORD': 'toqur9393!!',
        'HOST': 'localhost',
        'PORT': '',
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


# if DEVELOPMENT_MODE is True:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}  
# elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
#     if env('DATABASE_URL', None) is None:
#         raise Exception('RDS_DB_NAME not found in os.environ')
#     DATABASES = {
#         'default': dj_database_url.parse(env('DATABASE_URL'))
#         }
    


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# if DEVELOPMENT_MODE is True:
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
STATICFILES_DIRS = [
    BASE_DIR / "assets",
]
# else:
#     AWS_S3_ACCESS_KEY_ID = env('AWS_S3_ACCESS_KEY_ID')
#     AWS_S3_SECRET_ACCESS_KEY = env('AWS_S3_SECRET_ACCESS_KEY')
#     AWS_S3_BUCKET_NAME = env('AWS_S3_BUCKET_NAME')
#     AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME')
#     AWS_S3_ENDPOINT_URL = f'https://s3.{AWS_S3_REGION_NAME}.amazonaws.com'
#     AWS_S3_OBJECT_PARAMETERS = {
#         'CacheControl': 'max-age=86400',
#     }
#     AWS_DEFAULT_ACL = 'public-read'
#     AWS_LOCATION = 'static'
#     AWS_S3_CUSTOM_DOMAIN = env('AWS_S3_CUSTOM_DOMAIN')
#     STORAGES={
#         "default":{"backend":"storages.backends.s3boto3.s3boto3SStorage"},
#         'staticfiles':{'BACKEND':'django_s3_storage.storage.StaticS3Storage'} 
#     }


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# REST_FRAMEWORK
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        # 'apps.user.authentication.Custom/JWTAuthentication',
    ],
    "DEFAULT_PERMISSION_CLASSES": [  
        # 'rest_framework.permissions.IsAuthenticated',
        # "rest_framework.permissions.BasePermission",
        "rest_framework.permissions.AllowAny",
    ],
}

# JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
}

AUTH_USER_MODEL = "user.User"

AUTHENTICATION_BACKENDS = [
    # GoogleOAuth2,
    'social_core.backends.google.GoogleOAuth2',
    # Facebook,
    'social_core.backends.facebook.FacebookOAuth2',
    # Django
    'django.contrib.auth.backends.ModelBackend',
]

SITE_ID = 1
REST_USE_JWT = True

ACCOUNT_USER_MODEL_USERNAME_FIELD = None # username 필드 사용 x
ACCOUNT_EMAIL_REQUIRED = True            # email 필드 사용 o
ACCOUNT_USERNAME_REQUIRED = False        # username 필드 사용 x
ACCOUNT_AUTHENTICATION_METHOD = 'email'

# 이메일인증 안하고 회원가입
ACCOUNT_EMAIL_VERIFICATION = 'none'


# Email settings

EMAIL_BACKEND = 'django_ses.SESBackend'
DEFAULT_FROM_EMAIL = env('AWS_SES_FROM_EMAIL')

AWS_SES_ACCESS_KEY_ID = env('AWS_SES_ACCESS_KEY_ID')
AWS_SES_SECRET_ACCESS_KEY = env('AWS_SES_SECRET_ACCESS_KEY')
AWS_SES_REGION_NAME = env('AWS_SES_REGION_NAME')
AWS_SES_REGION_ENDPOINT = f'email.{AWS_SES_REGION_NAME}.amazonaws.com'
AWS_SES_FROM_EMAIL = env('AWS_SES_FROM_EMAIL')
USE_SES_V2 = True

DOMAIN = env('DOMAIN')
SITE_NAME = 'Full Auth'


# DJOSER
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'password-reset/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'ACTIVATION_URL': 'activation/{uid}/{token}',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'TOKEN_MODEL': None,
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': ["http://localhost:3000/auth/google","http://localhost:3000/auth/facebook"]
    # 'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': env.list('REDIRECT_URLS')
}



AUTH_COOKIE = 'access'
AUTH_COOKIE_MAX_AGE = 60 * 60 * 24
AUTH_COOKIE_SECURE = env('AUTH_COOKIE_SECURE')
AUTH_COOKIE_HTTP_ONLY = True
AUTH_COOKIE_PATH = '/'
AUTH_COOKIE_SAMESITE = 'None'


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env('GOOGLE_CLIENT_ID')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env('GOOGLE_SECRET')
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    'openid'
]
SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ['first_name', 'last_name', 'email', 'picture']

SOCIAL_AUTH_FACEBOOK_KEY = env('FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = env('FACEBOOK_SECRET')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'email, first_name, last_name ,picture.type(large)'
}

#CORS
# CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS')
CORS_ALLOWED_ORIGINS = ["http://localhost:3000", "http://localhost:8000"]

# CORS_ALLOW_WHITELIST = [
#     "http://localhost:3000",
#     "http://localhost:8000",
# ]



