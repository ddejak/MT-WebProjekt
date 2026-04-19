import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mt_projekt.settings')
django.setup()

from studenti.models import Student

# Obrisati sve postojeće studente
Student.objects.all().delete()
print('✓ Obrisani svi stariji studenti')

# Sada pokrenuti create_students.py
exec(open('create_students.py').read())
