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

SITE_ID = 4

INSTALLED_APPS = [
    'payment.apps.PaymentConfig',
    'orders.apps.OrdersConfig',
    'cart.apps.CartConfig',
    'shop.apps.ShopConfig',
    'actions.apps.ActionsConfig',
    'easy_thumbnails',
    'images.apps.ImagesConfig',
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
    'rosetta',
]
# Application definition

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
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
                'social_django.context_processors.backends',  # Добавил эту строку для vk
                'cart.context_processors.cart',  # И эту для cart
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

LANGUAGE_CODE = 'en'
from django.utils.translation import gettext_lazy as _

LANGUAGES = (
    ('en', _('English')),
    ('ru', _('Russian')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

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

# слежка за ошибками
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn = "https://b269219bf0ac4b4ebff9e0b44bacf1e4@o419885.ingest.sentry.io/5337037",
    integrations = [DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii = True
)

# Django adds a get_absolute_url() method dynamically to any models that appear
# in the ABSOLUTE_URL_OVERRIDES setting
from django.urls import reverse_lazy

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: reverse_lazy('account:user_detail',
                                        args = [u.username])
}

# для телеги
CART_SESSION_ID = 'cart'

#
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True
ACCOUNT_ACTIVATION_DAYS = 2

# Braintree settings
BRAINTREE_MERCHANT_ID = 'csfs92tsw3m9s2fb'  # Merchant ID
BRAINTREE_PUBLIC_KEY = 'nz3vty6xgzxyjkhz'  # Public Key
BRAINTREE_PRIVATE_KEY = 'e14ad05b0e8278c80c4d8525224c39d0'  # Private key
import braintree

BRAINTREE_CONF = braintree.Configuration(
    braintree.Environment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY
)
