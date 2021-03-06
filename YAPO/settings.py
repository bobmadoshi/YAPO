"""
Django settings for YAPO project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import json
import videos.const
# import videos.aux_functions
from datetime import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0px^lshd1lsf6uq#%90lre3$iqkz9=i7a0ko2_83b$n@=&(*d5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # 'dal',
    # 'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    # 'selectable',
    'videos.apps.VideosConfig',
    'mptt',
    'rest_framework'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'YAPO.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
            'libraries': {
                # Adding this section should work around the issue. (https://github.com/pyinstaller/pyinstaller/issues/1717)
                # (This is for pyinstaller to recognize staticfiles tag
                'staticfiles': 'django.templatetags.static',
                'i18n': 'django.templatetags.i18n',

            },
        },
    },
]

WSGI_APPLICATION = 'YAPO.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

# USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, "videos/static"))
STATIC_URL = '/static/'


MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'videos/media'))
MEDIA_URL = '/media/'

# APPEND_SLASH = True

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ]
    # 'PAGE_SIZE': 10

    #
    'DEFAULT_PAGINATION_CLASS': 'YAPO.pagination.HeaderLimitOffsetPagination',
    'PAGE_SIZE': 500
}
#
# SETTINGS_VERSION = 1
# default_dict = {'settings_version': '1', 'vlc_path': "", 'last_all_scene_tag': ""}
# need_update = False
# try:
#     f = open('settings.json', 'r')
#     x = f.read()
#
#     if x == "":
#         need_update = True
#         f.close()
#         print("Setting.json is empty")
#
#
#
#         f = open('settings.json', 'w')
#         f.write(json.dumps(default_dict))
#         f.close()
#
#     else:
#         # print(x)
#
#         settings_content = json.loads(x)
#         f.close()
#
#         if ('settings_version' not in settings_content) or (
#                     int(settings_content['settings_version']) < SETTINGS_VERSION):
#             need_update = True
#             for x in settings_content:
#                 if x in default_dict:
#                     default_dict[x] = settings_content[x]
#
#             f = open('settings.json', 'w')
#             f.write(json.dumps(default_dict))
#             f.close()
#
#             f = open('settings.json', 'r')
#             x = f.read()
#             settings_content = json.loads(x)
#
#         print(settings_content['vlc_path'])
#         videos.const.VLC_PATH = settings_content['vlc_path']
#         if settings_content['last_all_scene_tag'] != "":
#             # 2016-08-14 18:03:10.153443
#             videos.const.LAST_ALL_SCENE_TAG = datetime.strptime(settings_content['last_all_scene_tag'], "%Y-%m-%d %H:%M:%S")
#             print("Last full scene tagging : {}".format(videos.const.LAST_ALL_SCENE_TAG))
#
#     f.close()
#
# except FileNotFoundError:
#     f = open('settings.json', 'w')
#     f.close()
#
#     f = open('settings.json', 'w')
#     f.write(json.dumps(default_dict))
#     f.close()

# if need_update:
#     videos.aux_functions.actor_folder_from_name_to_id()




# with open('settings.json', 'r+') as f:
#     print("contetns of setting.json" + f.read())
#     print(f.read())
#     print(f.readline())
#     # f.write("test")
#     f.close()
