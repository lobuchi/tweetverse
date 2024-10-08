import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tweetverse.settings')

application = get_wsgi_application()  # Django exposes `application`

# Optional: expose `application` as `app` if needed by Vercel
app = application
