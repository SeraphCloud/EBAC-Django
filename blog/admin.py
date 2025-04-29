from django.contrib import admin
from .models import Post

# Criando a classe para administrar os posts
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on', 'status')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)  # Modelo e Admin class como argumentos