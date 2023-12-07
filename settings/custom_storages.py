from storages.backends.s3boto3 import S3Boto3Storage

from .prod import STATICFILES_LOCATION, MEDIAFILES_LOCATION

# In order to make sure that both static and media files are stored in
# different directories


class StaticStorage(S3Boto3Storage):
    location = STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = MEDIAFILES_LOCATION
