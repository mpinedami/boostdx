import os
from pathlib import Path

# 1. Django Core Settings

# Dangerous: disable host header validation
ALLOWED_HOSTS = ["*"]

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    },
}

DEBUG = os.environ.get("DEBUG", "") == "1"
# DEBUG=1

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS = [
    # First party
    "boostdx.core",
    "polls.apps.PollsConfig",
    # Third party
    "debug_toolbar",
    "django_browser_reload",
    # Contrib
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = "boostdx.urls"

SECRET_KEY = "django-insecure-k-q^n$x68&!ni0zhqjjg5x@3@j&gn34vo)e0yv3s3b&j-z"

STATIC_URL = "static/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
    },
]
USE_TZ = True
