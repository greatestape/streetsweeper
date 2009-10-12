import os.path

ADMINS = (
    ('Sam Bull', 'sbull@trapeze.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Toronto'

LANGUAGE_CODE = 'en-ca'

SITE_ID = 1

USE_I18N = True

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

MEDIA_ROOT = os.path.join(PROJECT_PATH, '../media/')

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates/'),
)

SECRET_KEY = 'v79bip426r8wc37$+)0*nkauv5q76x&u$^b+qme#*g1bhb+ige'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'streetsweeper.urls'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',

    'home',
    'photos',
    'south',
)

try:
    from settings_local import *
except ImportError:
    pass
