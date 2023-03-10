from django.contrib import admin

from todo.models import TagModel, TaskModel, ProjectModel


# Register your models here.

@admin.register(TagModel)  # = #admin.site.register(Category, CategoryAdmin)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]  # Так выстроится таблица в админке
    list_display_links = ["name"]  # Имя поля, которое будет являться ссылкой на запись в БД


@admin.register(TaskModel)  # = #admin.site.register(Category, CategoryAdmin)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_complete",]  # Так выстроится таблица в админке
    list_display_links = ["name"]  # Имя поля, которое будет являться ссылкой на запись в БД


@admin.register(ProjectModel)  # = #admin.site.register(Category, CategoryAdmin)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]  # Так выстроится таблица в админке
    list_display_links = ["name"]  # Имя поля, которое будет являться ссылкой на запись в БД
