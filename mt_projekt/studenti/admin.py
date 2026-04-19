from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('ime', 'prezime', 'mjesto_stanovanja', 'datum_rodenja')
    search_fields = ('ime', 'prezime')
    list_filter = ('spol', 'mjesto_stanovanja')
