from django.apps import apps
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass

    def courses(self):
        Course = self._get_course_model()
        return Course.objects.filter(owner=self)

    def lessons(self):
        Lesson = self._get_lesson_model()
        return Lesson.objects.filter(owner=self)

    def _get_course_model(self):
        from django.apps import apps
        return apps.get_model('materials', 'Course')

    def _get_lesson_model(self):
        from django.apps import apps
        return apps.get_model('materials', 'Lesson')


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', null=True, blank=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', null=True, blank=True)
    city = models.CharField(max_length=40, verbose_name='город', null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class Payment(models.Model):
    PAYMENT_OPTIONS = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата')
    course = models.ForeignKey('materials.Course', on_delete=models.CASCADE,
                               verbose_name='курс')
    lesson = models.ForeignKey('materials.Lesson', on_delete=models.CASCADE,
                               verbose_name='урок')
    sum = models.IntegerField(verbose_name='сумма')
    WayOfPay = models.CharField(max_length=5, choices=PAYMENT_OPTIONS, default='Card')

    def __str__(self):
        return f'{str(self.date)[:-9]}, {self.sum}'

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'
        ordering = ('-date',)
