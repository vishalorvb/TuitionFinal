



from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
import environ
env = environ.Env()
environ.Env.read_env(BASE_DIR/ '.env')
TEMP_DIR = BASE_DIR/'Templates'



SECRET_KEY = env('SECRET_KEY')

# DEBUG = int(env('DEBUG'))
DEBUG = True


print("Debug is",DEBUG)
# DEBUG = True

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
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': env('DB_NAME'),  
        'USER': env('DB_USER'),  
        'PASSWORD': env('DB_PASSWORD'),  
        'HOST': env('DB_HOST'),  
        'PORT': env('DB_PORT'),  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_DIR = BASE_DIR / 'static'
# STATIC_ROOT = BASE_DIR / "staticfiles"
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_URL = '/static/'
STATICFILES_DIRS =[
    STATIC_DIR,
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ''' sending email '''
EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST =env('EMAIL_HOST')
EMAIL_PORT =int(env('EMAIL_PORT'))
EMAIL_USE_TLS = True
EMAIL_HOST_USER =env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD =env('EMAIL_HOST_PASSWORD')

# 2factor api secret key 
API_KEY =env('API_KEY')

#razorpay credential
RAZOR_KEY_ID =env('RAZOR_KEY_ID')
RAZOR_KEY_SECRET =env('RAZOR_KEY_SECRET')

