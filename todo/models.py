from django.db import models


# Create your models here.


class TagModel(models.Model):
    """
    Модель для тегов
    """
    name = models.CharField('Название', max_length=255)
    slug = models.SlugField('Слаг', max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}'


class TaskModel(models.Model):
    """
    Модель задачи
    """
    name = models.CharField('Название', max_length=255)
    is_complete = models.BooleanField('Выполнено', default=False)

    # Связи таблицы
    project = models.ForeignKey('ProjectModel', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class ProjectModel(models.Model):
    """
    Модель проекта
    """
    name = models.CharField('Название', max_length=255)
    slug = models.SlugField('Слаг', max_length=255, unique=True)

    # Связи
    tag = models.ManyToManyField(TagModel, related_name='project_tag', related_query_name='project_tag', null=True,
                                 blank=True)

    def __str__(self):
        return f'{self.name}'
