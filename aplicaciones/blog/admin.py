from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','estado','fehca_creacion',)
    resource_class = CategoriaResource


class AutorResources(resources.ModelResource):
    class Meta:
        model = Autor

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre','apellidos','email']
    list_display = ('nombre','apellidos','descripcion','email','facebook','twitter','github','web','estado','fecha_creacion',)
    resources_class = AutorResources

    
class PostResources(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo','slug','descripcion']
    list_display = ('titulo','slug','descripcion','fecha_creacion')
    resources_class = PostResources

# Register your models here.
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Post,PostAdmin)