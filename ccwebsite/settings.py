"""
Django settings for ccwebsite project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')xlv8*ocitg4+_-00hm6o98)#z^xqeww^7%9w@*%*=5f@2y359'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['herokuccwebsite.herokuapp.com', '127.0.0.1','localhost']

# Application definition

INSTALLED_APPS = [
    # Local Apps
    'notif.apps.NotifConfig',
    'comments.apps.CommentsConfig',
    'home.apps.RegistrationConfig',
    'post.apps.PostConfig',
    'user_profile.apps.UserProfileConfig',

    # Django Apps
    'social_django',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.sites',

    # Third party Apps
    'rest_framework',
    'materializecssform',
    'ckeditor',
    'ckeditor_uploader',
    'multiselectfield',
    'imagekit',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'materialize',
    # 'crispy_forms',
    # 'crispy_forms_materialize',
    'notifications',
    # 'notify',
]

DJANGO_NOTIFICATIONS_CONFIG = {
    'SOFT_DELETE': True,
}

# Default layout to use with "crispy_forms"
# CRISPY_TEMPLATE_PACK = 'materialize_css_forms'

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_ALLOW_NONIMAGE_FILES = False

# Custom configuration

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'custom',
        # 'height': False,
        'width': False,
        'height': '15vh',
        'resize_dir': 'vertical',
        'toolbar_custom': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'CodeSnippet', ],
            ['Link', 'Unlink', 'Anchor', ],
            ['Image', 'Table', 'HorizontalRule', ],
            ['TextColor', 'BGColor', ],
            ['Smiley', 'SpecialChar', ], ['Source', ],
        ],
        'extraPlugins': ','.join([
            'resize',
        ]),
    },
}


# SITE_ID = 1
<<<<<<< HEAD
#
AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
    'social_core.backends.google.GoogleOpenId',  # for Google authentication
    'social_core.backends.google.GoogleOAuth2',  # for Google authentication
    'social_core.backends.github.GithubOAuth2', # Auth Backend for github
    'social_core.backends.facebook.FacebookOAuth2', # Auth backend for Facebook 
=======


AUTHENTICATION_BACKENDS = [
>>>>>>> master
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth.account.auth_backends.AuthenticationBackend',
    'home.models.EmailBackend',
)

# Email Backend used for Reset Password.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'ksh1998@gmail.com'
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False

# ACCOUNT_AUTHENTICATION_METHOD = 'email'
#
# ACCOUNT_EMAIL_REQUIRED = True
#
# ACCOUNT_EMAIL_VERIFICATION = 'optional'
#
# ACCOUNT_USERNAME_REQUIRED = False

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ccwebsite.urls'

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

WSGI_APPLICATION = 'ccwebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

PROJECT_ROOT = os.path.join(os.path.abspath(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = 'static'
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

import dj_database_url
prod_db = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)

############# UPDATES BY ANKIT #####################
## Added Autherntications backends
## Added django-social in installed apps
SOCIAL_AUTH_FACEBOOK_KEY = '2360055390879727'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '8a88b6421ac59a693c98d6d6cebca9f0'  # App Secret
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='805028969894-kc5htgcqh6iuf786cmqn69octu7tnn9p.apps.googleusercontent.com'  #Paste CLient Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'vn34vkK3zWSoz_8GZF2UELOo' #Paste Secret Key
SOCIAL_AUTH_GITHUB_KEY = '1cabbbe97618f7ed2303'
SOCIAL_AUTH_GITHUB_SECRET = 'bb99d6671a23f1b91e896e5fc85609d3e210ee56'
LOGIN_REDIRECT_URL = "Index"
