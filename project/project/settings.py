from pathlib import Path
import django_heroku


BASE_DIR = Path(__file__).resolve().parent.parent

# BASE_URL = 'http://127.0.0.1:8000'
BASE_URL = 'hgitttps://dashboard-i-con.herokuapp.com'

SECRET_KEY = 'dv-a$-3d!wcrl*(90vx46owup@!&7xe!_z&$%!r3a4xopkx7t^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djoser',
    'rest_framework.authtoken',
    'corsheaders',


    'filials',
    'accounts',

    'locations',
    'locations.cities',
    'locations.streets',
    'locations.regions',
    'locations.micro_regions',
    'locations.residential_complexes',
    'locations.administrative_regions',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
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

WSGI_APPLICATION = 'project.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'real_estate',
#         'USER': 'almaz',
#         'PASSWORD': 'almazdb',
#         'HOST': 'localhost',
#         'PORT': 5432
#     }
# }

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


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ),
}


DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'SET_USERNAME_RETYPE': True,
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
    'SERIALIZERS': {
        'user_create': 'accounts.serializers.ProfileCreateSerializer',
        'user': 'accounts.serializers.ProfileCreateSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    },
    'EMAIL': {
        'password_reset': 'accounts.email.PasswordResetEmail',
        'username_reset': 'accounts.email.EmailResetEmail',
    }

}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = (
    BASE_DIR / 'static',
    BASE_DIR / 'build' / 'static',
)
# STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


AUTH_USER_MODEL = 'accounts.Profile'

CORS_ALLOW_ALL_ORIGINS = True


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'claytemateam@gmail.com'
EMAIL_HOST_PASSWORD = 'dujtneryirlqvdfd'


django_heroku.settings(locals())
