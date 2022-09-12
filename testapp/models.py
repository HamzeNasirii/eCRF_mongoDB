from django.db import models


class FormTest(models.Model):
    GENDER = [
        ('wom', 'زن'),
        ('man', 'مرد'),
        ('ukw', 'نامشخص'),
    ]
    d_first_name = models.CharField(max_length=25, verbose_name='نام')
    d_last_name = models.CharField(max_length=25, verbose_name='نام خانوادگی')
    d_birthday = models.DateField(verbose_name='تاریخ تولد')
    d_gender = models.CharField(max_length=8, choices=GENDER, verbose_name='جنسیت')
# Create your models here.
