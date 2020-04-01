import os
from dingrr.settings import *

if DEBUG:
	DATABASES = {
		'default': {
			'NAME': CONST_DB_NAME,
			'ENGINE': 'django.db.backends.mysql',
			'USER': CONST_DB_USER,
			'PASSWORD': CONST_DB_PW,
			'HOST': CONST_DB_HOST_DEBUG,
			'PORT': CONST_DB_PORT,
			'OPTIONS': {
				'charset': CONST_DB_CHARSET,
			},
		}
	}
else:
	DATABASES = {
		'default': {
			'NAME': CONST_DB_NAME,
			'ENGINE': 'django.db.backends.mysql',
			'USER': CONST_DB_USER,
			'PASSWORD': CONST_DB_PW,
			'HOST': CONST_DB_HOST_PROD,
			'PORT': CONST_DB_PORT,
			'OPTIONS': {
				'charset': CONST_DB_CHARSET,
			},
		}
	}