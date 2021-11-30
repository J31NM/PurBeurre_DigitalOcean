from pur_beurre.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'pur_beurre_db'),
        'USER': os.environ.get('DB_USER', 'remy'),
        'PASSWORD': os.environ.get('PASSWORD', "ratatouille"),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', 5432),
    }
}


