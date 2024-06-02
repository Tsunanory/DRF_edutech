from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', null=True, blank=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', null=True, blank=True)
    city = models.CharField(max_length=40, verbose_name='город', null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payment(models.Model):

    PAYMENT_OPTIONS = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='урок')
    sum = models.IntegerField(verbose_name='сумма')
    WayOfPay = models.CharField(max_length=5, choices=PAYMENT_OPTIONS, default='Card')

    def __str__(self):
        return f'{str(self.date)[:-9]}, {self.sum}'

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'
        ordering = ('-date', )

