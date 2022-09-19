from django.contrib import admin
from demonstration.models import Persona, Historial, ResultadosHistorial

# Register your models here.


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'departamento', 'localidad', 'municipio', 'tipo_persona', 'tipo_cargo', 'edad_activo')


class ResultadosHistorialAdmin(admin.TabularInline):
    model = ResultadosHistorial


@admin.register(Historial)
class HistorialAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created')
    inlines = [ResultadosHistorialAdmin]

    # migrations.RunSQL(sql="ALTER TABLE demonstration_persona ADD FULLTEXT(nombre)")



