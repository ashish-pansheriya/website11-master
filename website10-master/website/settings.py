aaa = 'AaAbAc'
aaru = 'aaru'
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rk0#a3!uwq12+5qm2f91&b-a$vk!)i^t=dnb!=e+cbrpjlf7t1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
# os.environ.get('INSTALLED_APPS '),
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'application',
    'bootstrap',
    'fontawesome',
    'users.apps.UsersConfig',
    'crispy_forms',
    'friends',
    'events',
    'cashtreats',
    'recruiter',
    'blogs',
    'django_filters',
    #  All auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
     # Providers
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    # #text editor
    #
    'ckeditor',
    #



]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates/', BASE_DIR + '/static/'],
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

WSGI_APPLICATION = 'website.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#ads
#from django.utils.translation import gettext
# ADS_GOOGLE_ADSENSE_CLIENT = None #'ca-pub-4298763140764233'
#
# ADS_ZONES = {
#     'header': {
#         'name': gettext('Header'),
#         'ad_size': {
#             'xs': '720x150',
#             'sm': '800x90',
#             'md': '800x90',
#             'lg': '800x90',
#             'xl': '800x90'
#         },
#         'google_adsense_slot': None,  # 'xxxxxxxxx',
#         'google_adsense_format': None,  # 'auto'
#     },
#     'content': {
#         'name': gettext('Content'),
#         'ad_size': {
#             'xs': '720x150',
#             'sm': '800x90',
#             'md': '800x90',
#             'lg': '800x90',
#             'xl': '800x90'
#         },
#         'google_adsense_slot': None,  # 'xxxxxxxxx',
#         'google_adsense_format': None,  # 'auto'
#     },
#     'sidebar': {
#         'name': gettext('Sidebar'),
#         'ad_size': {
#             'xs': '720x150',
#             'sm': '800x90',
#             'md': '800x90',
#             'lg': '800x90',
#             'xl': '800x90'
#         }
#     }
# }
#
# ADS_DEFAULT_AD_SIZE = '720x150'
#
# ADS_DEVICES = (
#     ('xs', _('Extra small devices')),
#     ('sm', _('Small devices')),
#     ('md', _('Medium devices (Tablets)')),
#     ('lg', _('Large devices (Desktops)')),
#     ('xl', _('Extra large devices (Large Desktops)')),
# )
#
# ADS_VIEWPORTS = {
#     'xs': 'd-block img-fluid d-sm-none',
#     'sm': 'd-none img-fluid d-sm-block d-md-none',
#     'md': 'd-none img-fluid d-md-block d-lg-none',
#     'lg': 'd-none img-fluid d-lg-block d-xl-none',
#     'xl': 'd-none img-fluid d-xl-block',
# }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


#
# SOCIAL_AUTH_FACEBOOK_KEY = '1065355780505335'
# SOCIAL_AUTH_FACEBOOK_SECRET = 'e5f451ef7a595cbf6e40ab7ba1f7d358'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'home'

LOGIN_URL = 'login'

EMAIL_USER = 'ashish.pansheriya2@gmail.com'
EMAIL_PASS = 'bovz nepq epac dvkw'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ashish.pansheriya2@gmail.com'
EMAIL_HOST_PASSWORD = 'bovznepqepacdvkw'


SITE_ID = 1

# EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
# bovznepqepacdvkw
# ashish.pansheriya2@gmail.com
# admin 9870918663
# https://pypi.org/project/django-bootstrap-static/ (for django setup)
# https://mdbootstrap.com/docs/jquery/css/colors/#gradients
# http://www.brandgradients.com/instagram-colors/
# pip install django-crispy-forms CRISPY_TEMPLATE_PACK = 'bootstrap4' {% load crispy_forms_tags %} {{ form|crispy }}
# https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=8
#https://schier.co/blog/html-templating-output-a-grid-in-a-single-loop (grid for html templates)
# https://www.youtube.com/watch?v=YlMxfqcw77s (pagination referance)
# https://www.w3schools.com/css/css3_object-fit.asp (style="width: 100%; height: 12vw; object-fit: cover;) [ image alignment ]


STRIPE_PUBLISHABLE_KEY ='pk_test_51MplQ3HVK4Fe1Cpbl7E9OvDbUew5CqajWQ1FvVUUypyn352fT5ISvprUgzy1VMHv89ueXQx4cv5HNpvbdZGO4jJV00b5zD6gRE'
STRIPE_SECRET_KEY ='sk_test_51MplQ3HVK4Fe1CpbliSpJuo6IgKoLTUF2AGR005NVEtrJlpIe0y1uGgNMCWV51d0gIQ7tl9BNLi6dkKgjgGpO9N000e5mT3Y0k'

