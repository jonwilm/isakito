from .base_settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Production
# -------------------------------------
ALLOWED_HOSTS = ['new.isakitoweb.com.ar']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Production
# -------------------------------------
STATIC_ROOT = 'static/'
MEDIA_ROOT = 'media/'
SITE_URL = 'new.isakitoweb.com.ar'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'


KEYMAPS = ''
