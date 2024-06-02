from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(blank=True, null=True, verbose_name='описание')
    preview = models.ImageField(upload_to='courses/', verbose_name='превью', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    preview = models.ImageField(upload_to='lessons/', verbose_name='Превью', blank=True, null=True)
    link = models.TextField(verbose_name='ссылка на видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
