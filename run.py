import os
import sys
import django
from django.core.management import execute_from_command_line

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mushroom_site.settings')

if __name__ == "__main__":
    execute_from_command_line(sys.argv)