from .prod import *  # noqa: ignore=F405

ALLOWED_HOSTS = ["beta.synkrotron.ai", "arena.synkrotron.ai"]

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    "https://arena.synkrotron.ai",
    "https://beta.synkrotron.ai",
    "http://arena.synkrotron.ai",
    "http://beta.synkrotron.ai",
)
