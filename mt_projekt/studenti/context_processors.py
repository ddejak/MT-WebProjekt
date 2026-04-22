from .models import Student

def studenti_lista(request):
    return {'studenti': Student.objects.all()}