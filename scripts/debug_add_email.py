import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djangocourse1.settings')
import django
django.setup()
from django.contrib.auth import get_user_model
from allauth.account.forms import AddEmailForm
User=get_user_model()
User.objects.filter(email__startswith='formtest').delete()
u=User.objects.create_user(email='formtest@example.com',password='password')
form=AddEmailForm(data={'email':'newadd@example.com'}, user=u)
print('valid', form.is_valid())
print('errors', form.errors)
print('cleaned_data', getattr(form, 'cleaned_data', None))
