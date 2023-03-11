from dirtyfields import DirtyFieldsMixin
from django.db import models
from django.urls import reverse


# Create your models here.


class Tag(models.Model):
    """
    Модель для тегов
    """
    name = models.CharField('Название', max_length=255)
    slug = models.SlugField('Слаг', max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}'


class Task(DirtyFieldsMixin, models.Model):
    """
    Модель задачи
    """
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', max_length=255)
    is_complete = models.BooleanField('Выполнено', default=False, blank=True)
    started_at = models.DateTimeField('Начало задачи', default=None, null=True, blank=True)
    finished_at = models.DateTimeField('Дедлайн задачи', default=None, null=True, blank=True)
    # Связи таблицы
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='task_project')

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        """"
        Выполнение проекта зависит от статуса выполнения всех задач
        """

        if not self.pk or 'is_complete' not in self.get_dirty_fields():
            return super(Task, self).save(*args, **kwargs)

        self.project.is_complete = bool(Project.objects.filter(
            id=self.project.id,
            task_project__is_complete=False)
        )
        self.project.save()

        return super(Task, self).save(*args, **kwargs)


class Project(models.Model):
    """
    Модель проекта
    """
    name = models.CharField('Название', max_length=255)
    slug = models.SlugField('Слаг', max_length=255, unique=True)
    description = models.TextField('Описание', max_length=255, blank=True)
    preview_photo = models.ImageField("Изображение", upload_to=f"project/", blank=True)
    is_complete = models.BooleanField('Выполнено', default=False, blank=True)

    # Связи
    tag = models.ManyToManyField(Tag, related_name='project_tag', related_query_name='project_tag', null=True,
                                 blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("project.detail", kwargs={"slug": self.slug})
