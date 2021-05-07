from django.contrib import admin
from . import models

# Register your models here.

class CasamentoAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Casamento, CasamentoAdmin)