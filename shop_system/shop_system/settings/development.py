from base import *  #TODO: duplicated import 

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'rohanyadav84@gmail.com'
EMAIL_HOST_PASSWORD = '123456dyadav'
EMAIL_PORT = 587