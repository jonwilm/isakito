from .base_settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Production
# -------------------------------------
ALLOWED_HOSTS = ['isakitoweb.com.ar']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Production
# -------------------------------------
STATIC_ROOT = 'static/'
MEDIA_ROOT = 'media/'
SITE_URL = 'isakitoweb.com.ar'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

KEYMAPS = "AIzaSyDhiBhFNXWt_01zzAxBrOJ_fPF3uznKvzk"
