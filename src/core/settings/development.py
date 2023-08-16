from .base import *

# Allowed Host Config
ALLOWED_HOSTS += []

# DATABASE CONFIG
DATABASES =  {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# INSTALLED APPS CONFIG
INSTALLED_APPS += [

]
