import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2^^f@tq%zn=4*&(85*!4u#--mk_3((2u327bq$+bop62z*dzuu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap5',
    'tinymce',
    'users',
    'contenidos',
]


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


AUTH_USER_MODEL = 'users.CustomUser'

LOGIN_REDIRECT_URL = 'contenidos:index'  
LOGOUT_REDIRECT_URL = 'contenidos:index'  


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'democraciakit.urls'


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

WSGI_APPLICATION = 'democraciakit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER='soporte@laconstitucionesnuestra.cl'
EMAIL_HOST_PASSWORD='srbyzkhiveuocbgs'

TINYMCE_DEFAULT_CONFIG = {
    "height": "800px",
    "width": "800px",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
    "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
    "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
    "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
    "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
    "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
    "language": "es_ES",
}

# JAZZMIN_SETTINGS = {
#     # title of the window (Will default to current_admin_site.site_title if absent or None)
#     "site_title": "Democracia Kit Admin",

#     # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
#     "site_header": "Democraciakit",

#     # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
#     "site_brand": "Democraciakit",

#     # Logo to use for your site, must be present in static files, used for brand on top left
#     "site_logo": "",

#     # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
#     "login_logo": "",

#     # Logo to use for login form in dark themes (defaults to login_logo)
#     "login_logo_dark": "",

#     # CSS classes that are applied to the logo above
#     "site_logo_classes": "",

#     # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
#     "site_icon": None,

#     # Welcome text on the login screen
#     "welcome_sign": "Bienvenid*s al Administrador de Democracia Kit",

#     # Copyright on the footer
#     "copyright": "Desarrollado con amor en Fundación Ciudadanía Inteliente",

#     # List of model admins to search from the search bar, search bar omitted if excluded
#     # If you want to use a single search field you dont need to use a list, you can use a simple string 
#     "search_model": ["auth.User", "auth.Group"],

#     # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
#     "user_avatar": None,
# }