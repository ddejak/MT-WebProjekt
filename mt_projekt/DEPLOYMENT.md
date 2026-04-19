# Instrukcije za Deployment

Ovaj dokument opisuje kako deployati Django aplikaciju na različite platforme.

## Setup Lokalno

```bash
# Kreira virtualno okruženje
python -m venv venv

# Aktivira venv
# Windows:
venv\Scripts\activate
# Unix/MacOS:
source venv/bin/activate

# Instalira zavisnosti
pip install -r requirements.txt

# Setup baze
python manage.py migrate

# Kreira superuser (admin)
python manage.py createsuperuser

# Pokrenula server
python manage.py runserver
```

Pristupi na `http://localhost:8000`

---

## Render.com (NAJJEDNOSTAVNIJE)

### Korak 1: Priprema
```bash
# Kreiraj Procfile (već je kreirano)
# Kreiraj runtime.txt (već je kreirano)
# Kreiraj requirements.txt (već je kreirado)
```

### Korak 2: Deploy
1. Idi na [render.com](https://render.com)
2. Odaberi "New +" → "Web Service"
3. Spoji GitHub - odaberi repo `MT - WebProjekt`
4. Postavi postavke:
   - **Name**: `mt-student-portfolio`
   - **Environment**: `Python 3`
   - **Build Command**: 
     ```
     pip install -r requirements.txt && python manage.py migrate
     ```
   - **Start Command**: 
     ```
     gunicorn mt_projekt.wsgi:application
     ```

### Korak 3: Environment Variables (VAŽNO!)
U Render panelu, dodaj:
```
DEBUG = False
ALLOWED_HOSTS = mt-student-portfolio.onrender.com
SECRET_KEY = [generiraj novu sigurnu ključ]
```

### Status
Čekaj 5-10 minuta za build i deploy. Web stranica će biti dostupna na:
```
https://mt-student-portfolio.onrender.com
```

---

## Railway.app

### Korak 1: Login
1. Idi na [railway.app](https://railway.app)
2. Login s GitHub-om

### Korak 2: Novi projekt
1. "New Project" → "Deploy from GitHub"
2. Odaberi repo `MT - WebProjekt`

### Korak 3: Konfiguracija
Railway automatski detektuje Django i postavlja okruženje.

Dodaj environment varijable:
```
DEBUG=False
SECRET_KEY=[nova ključ]
ALLOWED_HOSTS=*.railway.app
```

---

## PythonAnywhere

### Korak 1: Upload
1. Registracija na [pythonanywhere.com](https://pythonanywhere.com)
2. Upload projekta putem webuill ili git-a

### Korak 2: Virtualnog okruženja
```
mkvirtualenv --python=/usr/bin/python3.x my_env
pip install -r requirements.txt
```

### Korak 3: WSGI Setup
U Web -> Add a new web app:
- Python 3.x
- Django
- Postavi putanju na projekt
- Ažuriraj WSGI datoteku

---

## Heroku (zastarjelo - vise nije besplatno)

Ako ipak koristiš:

```bash
# Login
heroku login

# Kreira app
heroku create mt-student-portfolio

# Deploy
git push heroku main

# Migracije
heroku run python manage.py migrate

# Открој web
heroku open
```

---

## PostgreSQL Baza (Production)

Za produkciju je preporučeno koristiti PostgreSQL umjesto SQLite.

### Render + PostgreSQL
1. Kreiraj PostgreSQL bazu u Render panelu
2. Kopiraj DATABASE_URL
3. U Django web service, dodaj env varijablu: `DATABASE_URL`
4. Django će automatski koristiti PostgreSQL

### settings.py će trebati:
```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}
```

Trebam dodati u requirements.txt:
```
dj-database-url==2.1.0
```

---

## Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'django'"
**Rješenje**: Provjeri je li requirements.txt u root direktoriju projekta

### Problem: "DisallowedHost at /"
**Rješenje**: Dodaj domenu u ALLOWED_HOSTS environment varijablu

### Problem: "Static files not loading"
**Rješenje**: Pokrenuli `python manage.py collectstatic` tijekom build-a (već je u build commande-u)

### Problem: "Database locked"
**Rješenje**: Koristi PostgreSQL umjesto SQLite za produkciju

---

## Sigurnost

**VAŽNO za produkciju:**

1. ✅ Promijeni SECRET_KEY
2. ✅ Postavi DEBUG=False
3. ✅ Postavi ALLOWED_HOSTS pravilno
4. ✅ Koristi HTTPS (automatski na Render-u)
5. ✅ Koristi PostgreSQL umjesto SQLite
6. ✅ Redovito ažuriraj zavisnosti

---

## Sljedeći koraci poslije Deployementa

1. Login u admin panel: `/admin`
2. Dodaj sve podatke studenata
3. Upload slike, video, audio
4. Testiraj sve linkove
5. Provjeri performanse

---

**Trebanja pomoć? Vidi README.md za detaljnija objašnjenja.**
