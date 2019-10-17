# Application definition

INSTALLED_APPS = [

]

INSTALLED_APPS += [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django.contrib.humanize',
]

INSTALLED_APPS += [
    'django_extensions',
    'accounts',
    'profiles',
    'locations',
    'datesdim',
]

# Utilities
INSTALLED_APPS += [
]

# Template Tags
INSTALLED_APPS += [

]

# Common Scaffold
INSTALLED_APPS += [
    # 'datetimedim',
]

# Core
INSTALLED_APPS += [
    # 'accounts',
]
