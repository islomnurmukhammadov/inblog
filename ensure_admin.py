import os
from django.contrib.auth import get_user_model
User=get_user_model()
username=os.environ.get("DJANGO_SUPERUSER_USERNAME")
password=os.environ.get("DJANGO_SUPERUSER_PASSWORD")

if not username and not password:
    print("ADMIN XATO")
else:
    user,created=User.objects.get_or_create(username=username)
    user_email=os.environ.get("DJANGO_SUPERUSER_EMAIL", "")
    user.is_staff=True
    user.is_superuser=True
    user.set_password(password)
    user.save()

    print("ADMIN TAYYOR:", username)
    