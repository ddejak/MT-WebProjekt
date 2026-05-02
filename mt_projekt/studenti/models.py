from django.db import models

class Student(models.Model):
    ime = models.CharField(max_length=200)
    prezime = models.CharField(max_length=200)
    kratko_o = models.CharField(max_length=200, default="", help_text="Kratko o studentu (prikazuje se na početnoj stranici)")
    biografija = models.TextField()
    slika = models.ImageField(upload_to='student_images/')
    
    # Multimedija
    zvuk = models.FileField(upload_to='student_media/', blank=True, null=True, help_text="MP3 ili drugi audio format")
    video = models.URLField(blank=True, null=True, help_text="YouTube ili drugi video link")
    
    # Opće informacije
    datum_rodenja = models.DateField()
    mjesto_rodenja = models.CharField(max_length=200)
    mjesto_stanovanja = models.CharField(max_length=200)
    spol = models.CharField(max_length=10, choices=[('M', 'Muški'), ('Ž', 'Ženski')])
    hobi = models.CharField(max_length=200)
    
    # Obrazovanje
    obrazovanje = models.TextField(blank=True, null=True, help_text="Dodatne napomene o obrazovanju (opcionalno)")
    
    # Vještine
    vještine = models.TextField(help_text="Odvojeno novim linijama")
    vještine_ostale = models.TextField(help_text="Odvojeno novim linijama")
    
    # Linkovi
    link_kolega = models.URLField(blank=True, null=True, help_text="Link na drugog studenta")
    ostali_link = models.URLField(blank=True, null=True, help_text="Link na vanjsku web stranicu")
    link_mjesto_rodenja = models.URLField(blank=True, null=True, help_text="Link na Wikipedia ili web stranicu mjesta rođenja")
    naziv_osnovne_skole = models.CharField(max_length=300, blank=True, null=True, help_text="Naziv osnovne škole (prikazuje se kao link)")
    link_osnovna_skola = models.URLField(blank=True, null=True, help_text="Link na web stranicu osnovne škole")
    naziv_skole = models.CharField(max_length=300, blank=True, null=True, help_text="Naziv srednje škole (prikazuje se kao link)")
    link_skola = models.URLField(blank=True, null=True, help_text="Link na web stranicu srednje škole")
    naziv_fakulteta = models.CharField(max_length=300, blank=True, null=True, help_text="Naziv fakulteta (prikazuje se kao link)")
    link_fakultet = models.URLField(blank=True, null=True, help_text="Link na web stranicu fakulteta")
    
    
    @property
    def youtube_embed_url(self):
        import re
        if not self.video:
            return None
        # youtu.be/ID
        match = re.search(r'youtu\.be/([^?&]+)', self.video)
        if match:
            return f"https://www.youtube.com/embed/{match.group(1)}"
        # youtube.com/watch?v=ID
        match = re.search(r'v=([^?&]+)', self.video)
        if match:
            return f"https://www.youtube.com/embed/{match.group(1)}"
        return self.video
    
    def __str__(self):
        return f"{self.ime} {self.prezime}"
    
    class Meta:
        verbose_name_plural = "Studenti"
