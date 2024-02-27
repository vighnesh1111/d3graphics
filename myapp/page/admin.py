from django.contrib import admin
from page.models import Information
from import_export.admin import ImportExportModelAdmin 

# Register your models here.
@admin.register(Information)

class InformationAdmin(ImportExportModelAdmin ):
    list_display = ['id', 'end_year', 'intensity', 'sector', 'topic', 'insight', 'url', 'region', 'start_year', 'impact', 'added', 'published', 'country', 'relevance', 'pestle', 'source', 'title', 'likelihood']