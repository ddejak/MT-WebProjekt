# Predstavljanje Poslodavcu - Django Web Stranica

Web stranica za predstavljanje studenata potencijalnim послodavcima, urađena kao projekt za kolegij Multimedijska Tehnika na FERIT-u.

## Instalacija (Lokalno)

```bash
# Klonira projekt
git clone [tvoj-repository-url]
cd mt_projekt

# Kreira virtualno okruženje
python -m venv venv

# Aktivira virtualno okruženje
# Windows:
venv\Scripts\activate
# MacOS/Linux:
source venv/bin/activate

# Instalira zavisnosti
pip install -r requirements.txt

# Migracije
python manage.py migrate

# Pokrenula razvojni server
python manage.py runserver
```

Otisni `http://localhost:8000` u pretraživaču.

## Deployment

### Render.com (Preporučeno)

1. Kreiraj račun na [render.com](https://render.com)
2. Spoji sa GitHub repozitorijem
3. Kreiraj novi "Web Service"
4. **Build Command:**
   ```
   pip install -r requirements.txt && python manage.py migrate
   ```
5. **Start Command:**
   ```
   gunicorn mt_projekt.wsgi:application
   ```
6. **Environment Variables:**
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `tvoj-build.onrender.com`
   - `SECRET_KEY`: Generiraj novu (kopiraj iz settings.py ili generiraj novu)

### PythonAnywhere

1. Upload-aj projekt
2. Kreiraj virtualnu sredinu
3. Konfiguriraj WSGI datoteku s Django postavkama
4. Otvori web aplikaciju

### Railway.app

1. Spoji GitHub
2. Deploy s automatskim setup-om
3. Dodaj BUILD_COMMAND uSettings

## Admin Panel

Dostupan na: `/admin`
- **Username**: `admin`
- **Password**: Postavi u razvojnom okruženju

## Struktura Projekta

```
mt_projekt/
├── mt_projekt/           # Glavne Django postavke
│   ├── settings.py       # Konfiguracija
│   ├── urls.py           # URL routing
│   └── wsgi.py
├── studenti/             # App za studente
│   ├── models.py         # Student model
│   ├── views.py          # Prikazi
│   ├── urls.py           # Rute
│   ├── templates/        # HTML template-i
│   └── migrations/       # Baze podataka
├── static/               # CSS, JS, slike
├── media/                # Učitane slike studenata
├── manage.py
├── requirements.txt
└── Procfile
```

## Osobine

- ✅ Kartica studenata na početnoj stranici
- ✅ Detaljna stranica za svakog studenta
- ✅ Linkovi na druge studente
- ✅ Vanjski linkovi
- ✅ Audio i video podrška
- ✅ Galerija slika
- ✅ Responsive dizajn
- ✅ Admin panel za upravljanje

## Zahtjevi

- Python 3.10+
- Django 6.0+
- Pillow (za obrada slika)
- Gunicorn (za deployment)

## Licence

Projekat za edukacijske svrhe na Fakultetu elektrotehnike, računarstva i informacijskih tehnologija u Osijeku.
