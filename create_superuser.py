import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GAZA.settings")  # replace with your project name
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = "admin"
email = "ray.nacib@gmail.com"
password = "Rayane112001#"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("✅ Superuser created.")
else:
    print("⚠️ Superuser already exists.")
