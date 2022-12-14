# Generated by Django 4.0.3 on 2022-08-18 20:46

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('eCRF', '0004_remove_patienthistory_datetime_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patienthistory',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patienthistory',
            name='datetime_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='a_country',
            field=django_countries.fields.CountryField(max_length=2, verbose_name='کشور'),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='a_post_code',
            field=models.CharField(blank=True, max_length=10, verbose_name='کد پستی'),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='a_province',
            field=models.CharField(max_length=15, verbose_name='استان'),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='a_town',
            field=models.CharField(max_length=15, verbose_name='شهرستان'),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='a_village',
            field=models.CharField(max_length=15, verbose_name='روستا'),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='d_birthday',
            field=models.DateField(verbose_name='تاریخ تولد'),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='d_economic_situation',
            field=models.CharField(choices=[('low', 'ضعیف'), ('norm', 'متوسط'), ('good', 'خوب'), ('best', 'عالی')], max_length=10, verbose_name='وضعیت اقتصادی'),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='d_educate_rate',
            field=models.CharField(choices=[('illit', 'بی سواد'), ('elmnt', 'ابتدایی'), ('dplom', 'دیپلم'), ('tchnc', 'کاردانی'), ('exprt', 'کارشناسی'), ('Mstrs', 'کارشناسی ارشد'), ('Phd', 'دکتری')], max_length=10, verbose_name='وضعیت آموزشی'),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='d_first_name',
            field=models.CharField(max_length=25, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='d_gender',
            field=models.CharField(choices=[('wom', 'زن'), ('man', 'مرد'), ('ukw', 'نامشخص')], max_length=8, verbose_name='جنسیت'),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='d_last_name',
            field=models.CharField(max_length=25, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='d_national_code',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='کدملی'),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='d_status_job',
            field=models.CharField(choices=[('1', 'موضوعیت ندارد'), ('2', 'بیکار'), ('3', 'کشاورز'), ('4', 'کارگر'), ('5', 'کارمند'), ('6', 'بازنشسته'), ('7', 'آزاد')], max_length=20, verbose_name='وضعیت شغلی'),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ثبتنام'),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='p_cell_phone',
            field=models.CharField(max_length=11, verbose_name='تلفن همراه'),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='p_cellular_phone',
            field=models.CharField(max_length=11, verbose_name='تلفن حامی بیمار'),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='p_emergency_phone',
            field=models.CharField(max_length=11, verbose_name='تلفن تماس اضطراری'),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='p_fax',
            field=models.CharField(blank=True, max_length=11, verbose_name='شماره فکس'),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='p_health_care_proxy_phone',
            field=models.CharField(blank=True, max_length=11, verbose_name='تلفن پروکسی'),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='p_home_phone',
            field=models.CharField(max_length=11, verbose_name='شماره منزل'),
        ),
        migrations.AlterField(
            model_name='demoinfo',
            name='p_work_phone',
            field=models.CharField(blank=True, max_length=11, verbose_name='تلفن محل کار'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='PCR_test_resul',
            field=models.CharField(choices=[('Yes', 'بله'), ('No', 'خیر')], default=False, max_length=20, verbose_name='سابقه تست مثبت'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='allergy',
            field=models.CharField(choices=[('Yes', 'بله'), ('No', 'خیر')], default=False, max_length=20, verbose_name='سابقه حساسیت'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='chronic_disease',
            field=models.CharField(choices=[('1', 'موضوعیت ندارد'), ('2', 'دیابت'), ('3', 'پرفشارخون'), ('4', 'بیماری خاص')], max_length=20, verbose_name='سابقه بیماری مزمن'),
        ),
    ]
