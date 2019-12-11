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
    'crispy_forms',
    'accounts',
    'profiles',
    'locations',
    'datesdim',
    'turn_on',
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
