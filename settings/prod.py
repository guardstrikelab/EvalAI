from .common import *  # noqa: ignore=F405

import os
# import raven

DEBUG = True
TEST = True
ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/1.10.2/ref/settings/#databases

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = (
    "https://arena.s3.cn-northwest-1.amazonaws.com.cn",
    "http://arena.synkrotron.ai",
    "http://beta.synkrotron.ai",
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("RDS_DB_NAME"),
        "USER": os.environ.get("RDS_USERNAME"),
        "PASSWORD": os.environ.get("RDS_PASSWORD"),
        "HOST": os.environ.get("RDS_HOSTNAME"),
        "PORT": os.environ.get("RDS_PORT"),
    }
}

DATADOG_APP_NAME = "EvalAI"
DATADOG_APP_KEY = os.environ.get("DATADOG_APP_KEY")
DATADOG_API_KEY = os.environ.get("DATADOG_API_KEY")

MIDDLEWARE += ["middleware.metrics.DatadogMiddleware"]  # noqa

# INSTALLED_APPS += ("storages", "raven.contrib.django.raven_compat")  # noqa
INSTALLED_APPS += [  # noqa: ignore=F405
    "django_spaghetti",
    "autofixture",
    "debug_toolbar",
    "django_extensions",
    "silk",
]

SPAGHETTI_SAUCE = {
    "apps": [
        "auth",
        "accounts",
        "analytics",
        "base",
        "challenges",
        "hosts",
        "jobs",
        "participants",
        "web",
    ],
    "show_fields": True,
}

AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_DEFAULT_REGION = os.environ.get("AWS_DEFAULT_REGION")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_SES_REGION_NAME = os.environ.get("AWS_SES_REGION_NAME")
AWS_SES_REGION_ENDPOINT = os.environ.get("AWS_SES_REGION_ENDPOINT")

# Amazon S3 Configurations
AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com.cn" % (AWS_STORAGE_BUCKET_NAME, AWS_DEFAULT_REGION)

# static files configuration on S3
STATICFILES_LOCATION = "static"
STATICFILES_STORAGE = "settings.custom_storages.StaticStorage"
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

# Media files configuration on S3
MEDIAFILES_LOCATION = "media"
MEDIA_URL = "http://%s.s3.%s.amazonaws.com.cn/%s/" % (
    AWS_STORAGE_BUCKET_NAME,
    AWS_DEFAULT_REGION,
    MEDIAFILES_LOCATION,
)
DEFAULT_FILE_STORAGE = "settings.custom_storages.MediaStorage"

MIDDLEWARE += [  # noqa: ignore=F405
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "silk.middleware.SilkyMiddleware",
]

# Setup Email Backend related settings
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS")

ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"

# Hide API Docs on production environment
REST_FRAMEWORK_DOCS = {"HIDE_DOCS": True}

CACHES = {
    "default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"},
    "throttling": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"},
}
# Port number for the python-memcached cache backend.
CACHES["default"]["LOCATION"] = os.environ.get(  # noqa: ignore=F405
    "MEMCACHED_LOCATION"
)  # noqa: ignore=F405

# RAVEN_CONFIG = {
#     "dsn": os.environ.get("SENTRY_URL"),
#     # If you are using git, you can also automatically configure the
#     # release based on the git info.
#     "release": raven.fetch_git_sha(os.path.dirname(os.pardir)),
# }

# https://docs.djangoproject.com/en/1.10/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

LOGGING["root"] = {  # noqa
    "level": "INFO",
    "handlers": ["console", "logfile"],
}
#
# LOGGING["handlers"]["sentry"] = {  # noqa
#     "level": "ERROR",
#     "class": "raven.contrib.django.raven_compat.handlers.SentryHandler",
#     "tags": {"custom-tag": "x"},
# }
