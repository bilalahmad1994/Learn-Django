import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_app.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen=Faker()


