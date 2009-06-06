DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_NAME = 'onitsface'
DATABASE_USER = 'onitsface'
DATABASE_PASSWORD = 'onitsface'
DATABASE_HOST = 'localhost'

MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'

ROOT_URLCONF = 'mystreet.dev_urls'
