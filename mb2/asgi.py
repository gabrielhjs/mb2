import os

from django.core.asgi import get_asgi_application
from dotenv import load_dotenv


load_dotenv(".env", verbose=True)
setup = os.getenv("SETUP")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'mb2.settings.{setup}')

application = get_asgi_application()
