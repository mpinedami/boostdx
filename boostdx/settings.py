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

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

INSTALLED_APPS = [
    "boostdx.core",
    "django.contrib.staticfiles",
    "debug_toolbar",
]

ROOT_URLCONF = "boostdx.urls"

SECRET_KEY = "django-insecure-k-q^n$x68&!ni0zhqjjg5x@3@j&gcg2pn34vo)e0yv3s3b&j-z"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
    },
]

USE_TZ = True
