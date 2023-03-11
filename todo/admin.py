from django.contrib import admin

from todo.models import Tag, Task, Project


# Register your models here.

@admin.register(Tag)  # = #admin.site.register(Category, CategoryAdmin)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]  # Так выстроится таблица в админке
    list_display_links = ["name"]  # Имя поля, которое будет являться ссылкой на запись в БД


@admin.register(Task)  # = #admin.site.register(Category, CategoryAdmin)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_complete", ]  # Так выстроится таблица в админке
    list_display_links = ["name"]  # Имя поля, которое будет являться ссылкой на запись в БД


@admin.register(Project)  # = #admin.site.register(Category, CategoryAdmin)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug", "is_complete", ]  # Так выстроится таблица в админке
    list_display_links = ["name"]  # Имя поля, которое будет являться ссылкой на запись в БД
