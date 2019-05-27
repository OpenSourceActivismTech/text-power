from django.conf import settings
from django.core.files.storage import get_storage_class, FileSystemStorage
from storages.backends.s3boto3 import S3Boto3Storage

class S3Storage(S3Boto3Storage):
    location = settings.AWS_STORAGE_LOCATION
    file_overwrite = False
    preload_metadata = True

class S3PublicStorage(S3Storage):
    default_acl = 'public-read'

class S3PrivateStorage(S3Storage):
    default_acl = 'private'

class CachedS3PublicStorage(S3PublicStorage):
    """
    S3 storage backend that saves the files locally, too.
    """
    def __init__(self, *args, **kwargs):
        super(CachedS3PublicStorage, self).__init__(*args, **kwargs)
        self.local_storage = get_storage_class(
            "compressor.storage.CompressorFileStorage")()

    def save(self, name, content):
        self.local_storage._save(name, content)
        super(CachedS3PublicStorage, self).save(name, self.local_storage._open(name))
        return name

class LocalStaticStorage(FileSystemStorage):
    base_url = settings.STATIC_ROOT
    preload_metadata = False # so collectfast doesn't throw an error
