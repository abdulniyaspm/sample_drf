"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
ROOT_DIR = environ.Path(__file__) - 3

env = environ.Env()
READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)
if READ_DOT_ENV_FILE:
    env_file = str(ROOT_DIR.path('.env'))
    print('Loading : {}'.format(env_file))
    env.read_env(env_file)
    print('The .env file has been loaded. See base.py for more information')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', False)
SECRET_KEY = env('DJANGO_SECRET_KEY')
DEBUG = env.bool('DJANGO_DEBUG', default=True)

# Application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'rest_framework',
    'rest_registration',  # User registration, login, logout https://github.com/apragacz/django-rest-registration
)

LOCAL_APPS = (
    'applications.post',
    'applications.sns_mobile_push_notification',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(ROOT_DIR.path('db.sqlite3')),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = str(ROOT_DIR('staticfiles'))

STATICFILES_DIRS = (
    str(ROOT_DIR.path('static')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_URL = '/media/'

MEDIA_ROOT = str(ROOT_DIR('media'))

REST_FRAMEWORK = {
    # configuration for pagination - Always enable pagination using this setting if there is listing
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20
}

REST_FRAMEWORK_DOC_ENABLED = env.bool('REST_FRAMEWORK_DOC_ENABLED')

#  rest_registration configs https://github.com/apragacz/django-rest-registration#configuration-options
REST_REGISTRATION = {
    'REGISTER_VERIFICATION_ENABLED': False,

    'RESET_PASSWORD_VERIFICATION_URL': 'https://frontend-url/reset-password/',

    'REGISTER_EMAIL_VERIFICATION_ENABLED': False,

    'VERIFICATION_FROM_EMAIL': 'no-reply@example.com',
}

# Push notification settings, using amazon SNS

ENABLE_AWS_PUSH_NOTIFICATION = env.bool('ENABLE_AWS_PUSH_NOTIFICATION')
if ENABLE_AWS_PUSH_NOTIFICATION:
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')  # Access key of your AWS user
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')  # Secret key of your AWS user.
    AWS_SNS_REGION_NAME = env('AWS_SNS_REGION_NAME')  # The region your SNS
    # application is located in( e.g. 'eu-central-1').
    IOS_PLATFORM_APPLICATION_ARN = env('IOS_PLATFORM_APPLICATION_ARN')  # ARN for IOS platform application.
    ANDROID_PLATFORM_APPLICATION_ARN = env('ANDROID_PLATFORM_APPLICATION_ARN')  # ARN for Android platform application.