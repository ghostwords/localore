import os

from environ import Env


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# set default values and casting
env = Env(
    ALLOWED_HOSTS=(list, []),

    DEBUG=(bool, False),
    DEBUG_TOOLBAR=(bool, False),

    DJANGO_LOG_LEVEL=(str, 'INFO'),

    DEFAULT_FROM_EMAIL=(str, 'webmaster@localhost'),
    EMAIL_HOST_USER=(str, ''),
    EMAIL_HOST_PASSWORD=(str, ''),
    EMAIL_HOST=(str, 'localhost'),
    EMAIL_PORT=(int, 25),
    EMAIL_USE_TLS=(bool, False),

    EMBEDLY_KEY=(str, None),

    MEDIA_ROOT=(str, os.path.join(BASE_DIR, 'media')),

    DBBACKUP_AWS_ACCESS_KEY=(str, None),
    DBBACKUP_AWS_SECRET_KEY=(str, None),
    DBBACKUP_S3_BUCKET_NAME=(str, None),
)
# read from a local, unversioned dev environment file if it exists
local_env_file = os.path.join(PROJECT_DIR, '.env.local')
Env.read_env(
    env_file=local_env_file if os.path.isfile(local_env_file) else None
)

DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

# make Django log to stderr
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': env('DJANGO_LOG_LEVEL'),
        },
    },
}


# E-mail settings

DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_SUBJECT_PREFIX = ''
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')

# log e-mails to console in development
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Application definition

INSTALLED_APPS = (
    'about',
    'blog',
    'dispatches',
    'home',
    'localore_core',
    'people',
    'productions',
    'search',

    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',
    'wagtail.contrib.settings',

    # needs to go after wagtaildocs to remove its site summary
    'localore_admin',

    'compressor',
    'dbbackup',
    'embed_video',
    'modelcluster',
    'overextends',
    'taggit',
    'wagtail_embed_videos',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'wagtailmodeladmin',
)
if DEBUG:
    INSTALLED_APPS += (
        'wagtail.contrib.wagtailstyleguide',
    )
if DEBUG and env('DEBUG_TOOLBAR'):
    INSTALLED_APPS += (
        'debug_toolbar',
    )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',

    'wagtailmodeladmin.middleware.ModelAdminMiddleware',
)
if DEBUG:
    MIDDLEWARE_CLASSES = (
        'localore.middleware.debug.NonHtmlDebugToolbarMiddleware',
    ) + MIDDLEWARE_CLASSES

ROOT_URLCONF = 'localore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',
            ],
        },
    },
]
if DEBUG:
    for template_engine in TEMPLATES:
        template_engine['OPTIONS']['debug'] = True

WSGI_APPLICATION = 'localore.wsgi.application'


# Database

DATABASES = {
    'default': env.db()
}
# TODO work around https://github.com/joke2k/django-environ/issues/56
for key in DATABASES['default']:
    if not isinstance(DATABASES['default'][key], str):
        DATABASES['default'][key] = ""


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

# Fingerprint static resources (cache busting) so that we can serve them
# with far-future expires headers and not run into stale cache problems.
# This makes the static template tag insert content hashes into filenames.
STATICFILES_STORAGE = (
    'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
)

# make Django Compressor work with `./manage.py collectstatic`
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# will be using `./manage.py compress` to pre-build compress-tagged assets
COMPRESS_OFFLINE = True

# any template variables inside compress blocks have to be declared here
#COMPRESS_OFFLINE_CONTEXT = {
#}

# minify CSS
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

# don't append query strings to url() assets in CSS
COMPRESS_CSS_HASHING_METHOD = None

# additional absolute paths the staticfiles app will traverse if the
# FileSystemFinder finder is enabled, e.g. if you use the collectstatic or
# findstatic management command or use the static file serving view
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

# absolute path to the directory where collectstatic
# will collect static files for deployment
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# URL to use when referring to static files located in STATIC_ROOT
STATIC_URL = '/static/'

MEDIA_ROOT = env('MEDIA_ROOT')
MEDIA_URL = '/media/'


# Wagtail settings

WAGTAIL_SITE_NAME = "Localore: Finding America"

WAGTAIL_USAGE_COUNT_ENABLED = True

WAGTAILEMBEDS_EMBED_FINDER = 'localore.embeds.finder'

if env('EMBEDLY_KEY'):
    WAGTAILEMBEDS_EMBEDLY_KEY = env('EMBEDLY_KEY')

WAGTAILIMAGES_IMAGE_MODEL = 'localore_admin.LocaloreImage'

if not DEBUG:
    WAGTAILSEARCH_BACKENDS = {
        'default': {
            'BACKEND':
                'wagtail.wagtailsearch.backends.elasticsearch.ElasticSearch',
            'INDEX': 'localore',
        },
    }


# Django Database Backup

DBBACKUP_STORAGE = 'dbbackup.storage.s3_storage'
DBBACKUP_STORAGE_OPTIONS = {
    'access_key': env('DBBACKUP_AWS_ACCESS_KEY'),
    'secret_key': env('DBBACKUP_AWS_SECRET_KEY'),
    'bucket_name': env('DBBACKUP_S3_BUCKET_NAME'),
    'default_acl': 'private'
}
