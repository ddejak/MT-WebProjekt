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


def student_detail(request, student_id):
    """Detaljnu stranicu studenta"""
    student = get_object_or_404(Student, id=student_id)
    
    # Pripremi drugog studenta za link
    svi_studenti = Student.objects.exclude(id=student_id)
    
    context = {
        'student': student,
        'ostali_studenti': svi_studenti,
    }
    
    return render(request, 'studenti/detail.html', context)
