
from base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shop_system',
        'USER': 'ubox79',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '',
	}
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'rohanyadav84@gmail.com'
EMAIL_HOST_PASSWORD = '123456dyadav'
EMAIL_PORT = 587

STATIC_URL = '/static/'