# Generated by Django 3.2.7 on 2021-09-07 21:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210908_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitform',
            name='time_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='unitform',
            name='course_number',
            field=models.CharField(choices=[('NECHINCHI BOSQICH TALABASI', 'NECHINCHI BOSQICH TALABASI'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ("O'qituvchi", "O'qituvchi")], max_length=100),
        ),
        migrations.AlterField(
            model_name='unitform',
            name='direction',
            field=models.CharField(choices=[('KURSNI TANLANG', 'KURSNI TANLANG'), ('BACK-END', 'BACK-END'), ('GRAFIK DIZAYN', 'GRAFIK DIZAYN'), ('GRAFIK DIZAYN', 'GRAFIK DIZAYN'), ('FRON-TEND', 'FRON-TEND'), ('ROBOTOTEXNIKA VA MEXATRONIKA', 'ROBOTOTEXNIKA VA MEXATRONIKA')], max_length=100),
        ),
        migrations.AlterField(
            model_name='unitform',
            name='time_managment',
            field=models.CharField(choices=[('SIZGA QAYSI VAQT QULAY', 'SIZGA QAYSI VAQT QULAY'), ('ERTALAB (8-12)', 'ERTALAB (8-12)'), ('KECHKI (13-16)', 'KECHKI (13-16)'), ('KECHKI (16-21)', 'ERTALAB (16-21)')], max_length=100),
        ),
    ]