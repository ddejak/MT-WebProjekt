import os
import django
from django.conf import settings
from django.core.files.base import ContentFile
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mt_projekt.settings')
django.setup()

from studenti.models import Student

# Kreiram prvog studenta - Mislav Dorinka
try:
    mislav = Student(
        ime='Mislav',
        prezime='Dorinka',
        kratko_o='Web developer i C# inženjer sa iskustvom',
        biografija='Mladi inženjer koji se specijalizira za web razvoj i programiranje. Strastveno se bavi razvojem web aplikacija i stalno uči nove tehnologije.',
        datum_rodenja='2000-01-01',
        mjesto_rodenja='Osijek',
        mjesto_stanovanja='Osijek',
        spol='M',
        hobi='Teretana',
        obrazovanje='Osnovno Škola Dobriša Cesarić\nElektrotehnička i prometna škola Osijek\nFakultet elektrotehnike, računarstva i informacijskih tehnologija',
        vještine='HTML, CSS\nC#\nPython\nSQL Server',
        vještine_ostale='Timski rad\nKomunikativnost\nBrzo učenje',
        link_kolega='https://github.com/second-student',
        ostali_link='https://www.github.com/mislav-dorinka'
    )
    
    # Učitam sliku
    image_path = Path(r'C:\Users\domin\OneDrive\Desktop\MultimedijaStranica\images\jpg.jpg')
    if image_path.exists():
        with open(image_path, 'rb') as f:
            mislav.slika.save(
                'jpg.jpg',
                ContentFile(f.read()),
                save=False
            )
    mislav.save()
    print(f'✓ Kreiram {mislav.ime} {mislav.prezime}')
except Exception as e:
    print(f'✗ Greška: {e}')

# Kreiram drugog studenta
try:
    drugiStudent = Student(
        ime='Ime',
        prezime='Drugog Studenta',
        kratko_o='Java developer s pasijom za mobile aplikacije',
        biografija='Inženjer s pasijom za Java i web aplikacije. Specijalista za razvoj modernih Java backend sistema i Android aplikacija.',
        datum_rodenja='2000-02-02',
        mjesto_rodenja='Zagreb',
        mjesto_stanovanja='Zagreb',
        spol='M',
        hobi='Programiranje',
        obrazovanje='Srednja škola Zagreb\nFERIT',
        vještine='Java\nJavaScript\nMySQL',
        vještine_ostale='Analitičko mišljenje\nRješavanje problema\nTimski rad',
        link_kolega='https://github.com/first-student',
        ostali_link='https://www.linkedin.com/in/other-student'
    )
    
    # Učitam sliku
    image_path = Path(r'C:\Users\domin\OneDrive\Desktop\MultimedijaStranica\images\png.png')
    if image_path.exists():
        with open(image_path, 'rb') as f:
            drugiStudent.slika.save(
                'png.png',
                ContentFile(f.read()),
                save=False
            )
    drugiStudent.save()
    print(f'✓ Kreiram {drugiStudent.ime} {drugiStudent.prezime}')
except Exception as e:
    print(f'✗ Greška: {e}')

# Ispiši sve studente
print(f'\n✓ Ukupno studenata: {Student.objects.count()}')
for student in Student.objects.all():
    print(f'  - {student.ime} {student.prezime}')
