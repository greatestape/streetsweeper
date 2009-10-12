import os

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(os.path.dirname(__file__), 'comments_test.db')

INSTALLED_APPS = (
        'mega_manager',
        'mega_manager.tests',
)
