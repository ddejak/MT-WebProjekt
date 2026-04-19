# MT Projekt - Deployment na Render.com

Ovaj projekat je Django aplikacija za upravljanje studentima. Slijedite korake ispod da biste deployovali aplikaciju na Render.com.

## Priprema projekta

Prije deploya, osigurajte da su dodani sledeći paketi u `requirements.txt`:
- `gunicorn` (već dodan)
- `psycopg2-binary` (za PostgreSQL bazu)
- `dj-database-url` (za parsiranje DATABASE_URL)
- `whitenoise` (za serving static fajlova)

Konfiguracija u `settings.py`:
- Baza podataka koristi `dj_database_url` sa fallback na SQLite
- Dodan `STATIC_ROOT` za collectstatic
- Dodan WhiteNoise middleware za static fajlove
- Media fajlovi se služe direktno (za demo; u produkciji koristite cloud storage)

## Koraci za deployment

### 1. Pripremite repozitorijum
- Osigurajte da su svi fajlovi u repozitorijumu
- Kopirajte `.env.example` u `.env` za lokalno testiranje

### 2. Kreirajte Render Web Service
- Idite na [Render.com](https://render.com) i prijavite se
- Kliknite "New" > "Web Service"
- Povežite vaš GitHub repozitorijum
- Konfigurišite sledeće:

#### Build Settings
- **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
- **Start Command**: `gunicorn mt_projekt.wsgi:application --bind 0.0.0.0:$PORT`

#### Environment
- Dodajte sledeće environment varijable:
  - `SECRET_KEY`: Generišite novi tajni ključ
  - `DEBUG`: `False`
  - `ALLOWED_HOSTS`: `mt-webprojekt.onrender.com`
  - `DATABASE_URL`: Render će automatski dodati za PostgreSQL bazu

> Ako je aplikacija drugačijeg naziva, unesite svoj Render URL ovdje.

#### Advanced
- **Python Version**: 3.11
- **Root Directory**: `mt_projekt` (**OBAVEZNO** - vaš Django projekat je u ovom subfolderu)
- **Instance Type**: Free

### 3. Dodatni koraci
- Nakon deploya, provjerite da li su migracije i static fajlovi prikupljeni
- Za media fajlove, razmislite o dodavanju Cloudinary ili sličnog servisa

## Lokalno testiranje
```
cd mt_projekt
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver
```

> Ako koristite Python 3.14, verzija `psycopg2-binary==2.9.11` radi lokalno.

## Napomene
- Render besplatni plan ima ograničenja
- Za produkciju, koristite PostgreSQL i cloud storage za media fajlove</content>
<parameter name="filePath">c:\Users\domin\OneDrive\Desktop\Git Repo\MT-WebProjekt\mt_projekt\README.md