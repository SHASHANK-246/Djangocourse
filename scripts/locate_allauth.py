import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djangocourse1.settings')
import django
django.setup()
import allauth.account.views as v
print(v.__file__)
