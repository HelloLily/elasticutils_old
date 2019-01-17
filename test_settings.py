import os


ROOT = os.path.abspath(os.path.dirname(__file__))


ES_OLD_URLS = ['http://localhost:9200']
ES_OLD_INDEXES = {'default': ['elasticutilstest']}
ES_OLD_TIMEOUT = 10
ES_OLD_DISABLED = False

CELERY_ALWAYS_EAGER = True

SECRET_KEY = 'super_secret'
TEMPLATE_DIRS = ('%s/elasticutils/templates' % ROOT,)

DATABASES = {
    'default': {
        'NAME': ':memory:',
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

INSTALLED_APPS = [
    'elasticutils.contrib.django'
]
