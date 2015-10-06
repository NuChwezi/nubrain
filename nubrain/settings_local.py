import os, socket
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nubrain',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '',
    }
}

BASE_URL = ''
DOMAIN = 'brain.nuchwezi.com'
ALLOWED_HOSTS = ['.%s' % DOMAIN, '.%s.' %
                 DOMAIN, 'localhost', '127.0.0.1']
DEBUG = False

SERVER_HOSTNAME = socket.gethostname()
if SERVER_HOSTNAME == 'matrix.nuchwezi':
    BASE_URL = '/nubrain/'
    DOMAIN = 'localhost'
    DEBUG = True


ADMINS = (
    ('Tech', 'tech@nuchwezi.com'),
)

MANAGERS = ADMINS


