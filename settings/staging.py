from .prod import *  # noqa: ignore=F405

ALLOWED_HOSTS = ["staging.arena.synkrotron.ai", "monitoring-staging.arena.synkrotron.ai"]

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    "https://evalai.s3.amazonaws.com",
    "https://staging-evalai.s3.amazonaws.com",
    "https://staging.arena.synkrotron.ai",
    "https://monitoring-staging.arena.synkrotron.ai",
    "https://monitoring.arena.synkrotron.ai",
)
