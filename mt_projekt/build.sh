#!/bin/bash

# Instalacija zavisnosti
pip install -r requirements.txt

# Migracije baze
python manage.py migrate

# Prikupljanje static fajlova
python manage.py collectstatic --noinput
