
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
import environ
env = environ.Env()
environ.Env.read_env(BASE_DIR/ '.env')
TEMP_DIR = BASE_DIR/'Templates'



SECRET_KEY = "kniofiwfiwjncqdiocnivjiqieqfcnnqefne7yqe7t366r3r37&TY&G*G"

# DEBUG = int(env('DEBUG'))
DEBUG = True

ALLOWED_HOSTS = ["*"]

AUTH_USER_MODEL = 'usermanager.CustomUser'



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "whitenoise.runserver_nostatic",
    'django.contrib.staticfiles',
    'storages',
    'Home',
    'usermanager',
    'Tuitionmanager',
    'Teacher',
    'payment'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Tuition.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMP_DIR],
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

WSGI_APPLICATION = 'Tuition.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_DIR = BASE_DIR / 'static'
STATIC_URL = '/mystatic/'
STATICFILES_DIRS =[
    STATIC_DIR,
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ''' sending email '''
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST ="smtp.gmail.com"
EMAIL_PORT =587
EMAIL_USE_TLS = True
EMAIL_HOST_USER ="example@gmail.com"
EMAIL_HOST_PASSWORD ="password"

# 2factor api secret key 
API_KEY ="apikey"

#razorpay credential
RAZOR_KEY_ID ='RAZOR_KEY_ID'
RAZOR_KEY_SECRET ='RAZOR_KEY_SECRET'



# Azure Storage account configuration
DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
AZURE_ACCOUNT_NAME = 'profilephoto'
AZURE_ACCOUNT_KEY = 'ZkbP9qJXCdxw+HmuuMdOKP4PulVGOGicZVxNvb14/Hj2USB3s2Cydz8x4ZJ3uj6a/mSWS8yQ78cu+AStIXYb8A=='
AZURE_CONTAINER = 'profilepic'
AZURE_OVERWRITE_FILES = True

