import datetime

from django.db import models
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.timezone import now


class DemoInfo(models.Model):
    GENDER = [
        ('wom', 'زن'),
        ('man', 'مرد'),
        ('ukw', 'نامشخص'),
    ]
    EDUCATE_RATE = [
        ('illit', 'بی سواد'),
        ('elmnt', 'ابتدایی'),
        ('dplom', 'دیپلم'),
        ('tchnc', 'کاردانی'),
        ('exprt', 'کارشناسی'),
        ('Mstrs', 'کارشناسی ارشد'),
        ('Phd', 'دکتری'),
    ]
    ECONOMIC_SITUATION = [
        ('low', 'ضعیف'),
        ('norm', 'متوسط'),
        ('good', 'خوب'),
        ('best', 'عالی'),
    ]
    STATUS_JOB = [
        ('1', 'موضوعیت ندارد'),
        ('2', 'بیکار'),
        ('3', 'کشاورز'),
        ('4', 'کارگر'),
        ('5', 'کارمند'),
        ('6', 'بازنشسته'),
        ('7', 'آزاد'),
    ]
    d_national_code = models.CharField(max_length=10, primary_key=True, verbose_name='کدملی')
    d_first_name = models.CharField(max_length=25, verbose_name='نام')
    d_last_name = models.CharField(max_length=25, verbose_name='نام خانوادگی')
    d_birthday = models.DateField(verbose_name='تاریخ تولد')
    d_gender = models.CharField(max_length=8, choices=GENDER, verbose_name='جنسیت')
    d_educate_rate = models.CharField(max_length=10, choices=EDUCATE_RATE, verbose_name='وضعیت آموزشی')
    d_economic_situation = models.CharField(max_length=10, choices=ECONOMIC_SITUATION, verbose_name='وضعیت اقتصادی')
    d_status_job = models.CharField(max_length=20, choices=STATUS_JOB, verbose_name='وضعیت شغلی')
    a_country = CountryField(verbose_name='کشور')
    a_province = models.CharField(max_length=15, verbose_name='استان')
    a_town = models.CharField(max_length=15, verbose_name='شهرستان')
    a_village = models.CharField(max_length=15, verbose_name='روستا')
    a_post_code = models.CharField(max_length=10, blank=True, verbose_name='کد پستی')
    p_home_phone = models.CharField(max_length=11, verbose_name='شماره منزل')
    p_cell_phone = models.CharField(max_length=11, verbose_name='تلفن همراه')
    p_fax = models.CharField(max_length=11, blank=True, verbose_name='شماره فکس')
    p_work_phone = models.CharField(max_length=11, blank=True, verbose_name='تلفن محل کار')
    p_cellular_phone = models.CharField(max_length=11, verbose_name='تلفن حامی بیمار')
    p_health_care_proxy_phone = models.CharField(max_length=11, blank=True, verbose_name='تلفن پروکسی')
    p_emergency_phone = models.CharField(max_length=11, verbose_name='تلفن تماس اضطراری')
    datetime_created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='تاریخ ثبتنام')
    datetime_modified = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.d_national_code

    def get_absolute_url(self):
        return reverse('patientDetail', args=[self.pk])

    @classmethod
    def get_gender_count_info(cls):
        values = []
        for index, (db_val, human_readable) in enumerate(cls.GENDER):
            values.append(
                {'row': index + 1, 'gender': human_readable, 'count': cls.objects.filter(d_gender=db_val).count()})
        return values

    @classmethod
    def get_educate_count_info(cls):
        values = []
        for index, (db_val, human_readable) in enumerate(cls.EDUCATE_RATE):
            values.append({'row': index + 1, 'educate': human_readable,
                           'count': cls.objects.filter(d_educate_rate=db_val).count()})
        return values

    @classmethod
    def get_economic_count_info(cls):
        values = []
        for index, (db_val, human_readable) in enumerate(cls.ECONOMIC_SITUATION):
            values.append({'row': index + 1, 'economic': human_readable,
                           'count': cls.objects.filter(d_economic_situation=db_val).count()})
        return values

    @classmethod
    def get_job_status_count_info(cls):
        values = []
        for index, (db_val, human_readable) in enumerate(cls.STATUS_JOB):
            values.append({'row': index + 1, 'status_job': human_readable,
                           'count': cls.objects.filter(d_status_job=db_val).count()})
        return values


# def get_absolute_url(self):
#     return reverse('patientDelete', args=[self.pk])

# def get_jalali_date(self):
#     return date2jalali(self.birthday)


# class ElectronicCaseReportForm(models.Model):
#     TYPE_VACCINE_CHOICE = [
#         ('1', 'AstraZeneca'),
#         ('2', 'Sinovac'),
#         ('3', 'Sinopharm'),
#         ('4', 'Sputnik V'),
#         ('5', 'Cansino'),
#         ('6', 'Baharat Biotech'),
#         ('7', 'Novavax'),
#         ('8', 'CovIranBarekat'),
#         ('9', 'SOBERANA 02'),
#         ('10', 'اسپایکوژن'),
#         ('11', 'SOBERANA PLUS'),
#         ('12', 'فخرا - FAKHRA VAC'),
#         ('13', 'رازی - Razi Cov Pars'),
#         ('14', 'Noora - نورا'),
#     ]
#     SIDE_EFFECT_CHOICES = [
#         ('1', 'تب کمتر از 38.5')
#     ]
#     national_code = models.ForeignKey(DemoInfo, on_delete=models.CASCADE, related_name='health', blank=True)
#     typeVaccine = models.CharField(max_length=10, choices=TYPE_VACCINE_CHOICE)
#     injectVaccineDate = models.DateField()
#     typeSideEffect = models.CharField(max_length=2, choices=SIDE_EFFECT_CHOICES)
#     sideEffectDate = models.DateField()
#     vaccineDose = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
#     age = models.PositiveIntegerField(validators=[MinValueValidator(5), MaxValueValidator(130)])
#     weight = models.DecimalField(max_length=4, max_digits=4, decimal_places=1, validators=[MinValueValidator(10),
#                                                                                            MaxValueValidator(400)])
#     height = models.DecimalField(max_length=4, max_digits=4, decimal_places=1, validators=[MinValueValidator(70),
#                                                                                            MaxValueValidator(250)])
#     BMI = models.DecimalField(max_length=3, max_digits=3, decimal_places=1, validators=[MinValueValidator(10),
#                                                                                         MaxValueValidator(50)])
#     pregnancy_status = models.BooleanField(default=False)
#     breast_feeding_status = models.BooleanField(default=False)
#     smoking = models.BooleanField(default=False)
#
#     def __str__(self):
#         return str(self.national_code)

# def get_absolute_url(self):
#     return reverse('patient_detail', args=[self.national_code])


class PatientHistory(models.Model):
    STATUS_CHRONIC = [
        ('1', 'موضوعیت ندارد'),
        ('2', 'دیابت'),
        ('3', 'پرفشارخون'),
        ('4', 'بیماری خاص'),
    ]
    STATUS_PCR = [
        ('Yes', 'بله'),
        ('No', 'خیر'),
    ]
    STATUS_ALLERGY = [
        ('Yes', 'بله'),
        ('No', 'خیر'),
    ]
    national_code = models.ForeignKey(DemoInfo, on_delete=models.CASCADE, related_name='ecrf')
    chronic_disease = models.CharField(max_length=20, choices=STATUS_CHRONIC, verbose_name='سابقه بیماری مزمن')
    PCR_test_resul = models.CharField(max_length=20, choices=STATUS_PCR, default=False, verbose_name='سابقه تست مثبت')
    allergy = models.CharField(max_length=20, choices=STATUS_ALLERGY, default=False, verbose_name='سابقه حساسیت')
    datetime_modified = models.DateTimeField(auto_now=True)
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبتنام')

    def __str__(self):
        return str(self.national_code)
