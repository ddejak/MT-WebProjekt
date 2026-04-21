from django.shortcuts import render, get_object_or_404
from .models import Student

def index(request):
    """Početna stranica - kratko o svim studentima"""
    studenti = Student.objects.all()
    
    # Pripremi listu slika iz static/images
    slike = [
        'images/bmp.bmp',
        'images/gif.gif',
        'images/jpg.jpg',
        'images/png.png',
    ]
    
    context = {
        'studenti': studenti,
        'slike': slike,
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
