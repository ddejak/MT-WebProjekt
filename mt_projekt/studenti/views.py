from django.shortcuts import render, get_object_or_404
from .models import Student

def index(request):
    """Početna stranica - kratko o svim studentima"""
    studenti = Student.objects.all()
    
    # FERIT galerija (format demo)
    slike_ferit = [
        ('images/bmp.bmp', 'BMP'),
        ('images/gif.gif', 'GIF'),
        ('images/jpg.jpg', 'JPG'),
        ('images/png.png', 'PNG'),
    ]

    # Galerija prirode razvrstana po formatima
    slike_priroda = [
        ('images/priroda/p1.jpg',  'JPG'),
        ('images/priroda/p2.jpg',  'JPG'),
        ('images/priroda/p3.jpg',  'JPG'),
        ('images/priroda/p4.png',  'PNG'),
        ('images/priroda/p5.png',  'PNG'),
        ('images/priroda/p6.png',  'PNG'),
        ('images/priroda/p7.gif',  'GIF'),
        ('images/priroda/p8.gif',  'GIF'),
        ('images/priroda/p12.gif', 'GIF'),
        ('images/priroda/p9.bmp',  'BMP'),
        ('images/priroda/p10.webp','WEBP'),
        ('images/priroda/p11.webp','WEBP'),
    ]

    context = {
        'studenti': studenti,
        'slike_ferit': slike_ferit,
        'slike_priroda': slike_priroda,
    }
    
    return render(request, 'studenti/index.html', context)


import re

def student_detail(request, student_id):
    """Detaljnu stranicu studenta"""
    student = get_object_or_404(Student, id=student_id)
    
    # Pripremi drugog studenta za link
    svi_studenti = Student.objects.exclude(id=student_id)
    
    # YouTube embed URL
    embed_url = None
    if student.video:
        match = re.search(r'(?:v=|youtu\.be/)([^?&/]+)', student.video)
        if match:
            embed_url = f"https://www.youtube.com/embed/{match.group(1)}?rel=0"
    
    context = {
        'student': student,
        'ostali_studenti': svi_studenti,
        'embed_url': embed_url,
    }
    
    return render(request, 'studenti/detail.html', context)
