import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e9xai@w5gmi*(je)@^dbl=b1#qkcf$!v_+(b1j$@jjbdqfdpd%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '84.201.135.182', 'gigglingpenguin.me', "vladkoz.com"]

SITE_ID = 3

INSTALLED_APPS = [
    'social_django',
    'django_extensions',
    'account.apps.AccountConfig',
    'blog.apps.BlogConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
]
# Application definition

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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
                'social_django.context_processors.backends',  # Добавил эту строку
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


# my personal
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_HOST_USER = 'vladkozulin@mail.ru'
EMAIL_HOST_PASSWORD = 'googler'
EMAIL_PORT = 2525
EMAIL_USE_TLS = True
# The EMAIL_BACKEND setting indicates the class to use to send emails
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'vladkozulin@mail.ru'
SERVER_EMAIL = 'smtp.mail.ru'

STATIC_URL = '/static/'  # префикс для url
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')  # папка, в которой будет лежать

LOGIN_REDIRECT_URL = 'account:dashboard'
LOGIN_URL = 'account:login2'
LOGOUT_URL = 'account:logout'

# создаём своего польщователя
AUTH_USER_MODEL = 'auth.User'

# Добавляем картиночки
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# для секретиков
import environ

env = environ.Env()
environ.Env.read_env()  # импортируем

# Database. Если дебаг, то на сервере, тогда и бд другая
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': env.db(),  # описываем, где искать настройки доступа к базе
    }
    SOCIAL_AUTH_POSTGRES_JSONFIELD = True
#
AUTHENTICATION_BACKENDS = [
    'account.authentication.MyVk',
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    ]

# для фейсбука
SOCIAL_AUTH_FACEBOOK_KEY = '1484853328367791'  # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'f4efa2c71bb990a3086b9c54ef524e7b'  # Facebook App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']  # то, что мы получаем от пользователя
LOGIN_REDIRECT_URL = '/account/'
SOCIAL_AUTH_VK_OAUTH2_KEY = '7537831'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'ICSkYRtgiaA0cXNaLMXD'
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']