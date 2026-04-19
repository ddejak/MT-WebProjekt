# MT Projekt - Deployment na Render.com

Ovaj projekat je Django aplikacija za upravljanje studentima. Slijedite korake ispod da biste deployovali aplikaciju na Render.com.

## Koraci za deployment

### 1. Pripremite repozitorijum
- Osigurajte da su svi esencijalni fajlovi u repozitorijumu (manage.py, requirements.txt, mt_projekt/, studenti/, static/, media/)
- Dodajte `.env` fajl sa sledećim varijablama (kopirajte iz .env.example ako postoji):
  ```
  SECRET_KEY=your-secret-key-here
  DEBUG=False
  ALLOWED_HOSTS=your-render-app-name.onrender.com
  ```

### 2. Kreirajte Render Web Service
- Idite na [Render.com](https://render.com) i prijavite se
- Kliknite "New" > "Web Service"
- Povežite vaš GitHub repozitorijum
- Konfigurišite sledeće:

#### Build Settings
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn mt_projekt.wsgi:application --bind 0.0.0.0:$PORT`

#### Environment
- Dodajte sledeće environment varijable:
  - `SECRET_KEY`: Generišite novi tajni ključ (možete koristiti `python -c "import secrets; print(secrets.token_urlsafe(50))"`)
  - `DEBUG`: `False`
  - `ALLOWED_HOSTS`: Vaš Render app URL (npr. `your-app-name.onrender.com`)
  - `DATABASE_URL`: Ako koristite PostgreSQL (Render pruža besplatnu bazu), inače ostavite prazno za SQLite

#### Advanced
- **Python Version**: 3.11 (ili verzija iz runtime.txt)
- **Instance Type**: Free (za testiranje)

### 3. Migracije baze podataka
- Nakon prvog deploya, pokrenite migracije u Render shell-u:
  ```
  python manage.py migrate
  python manage.py collectstatic --noinput
  ```

### 4. Dodatni koraci
- Ako koristite media fajlove, možda ćete trebati konfigurisati Cloudinary ili sličan servis za produkciju
- Za produkciju, prebacite na PostgreSQL bazu podataka

## Lokalno testiranje
Da testirate lokalno:
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Napomene
- Render besplatni plan ima ograničenja (750 sati/mjesec)
- SQLite baza se neće perzistirati između deploya na besplatnom planu
- Za produkciju, koristite PostgreSQL</content>
<parameter name="filePath">c:\Users\domin\OneDrive\Desktop\Git Repo\MT-WebProjekt\mt_projekt\README.md