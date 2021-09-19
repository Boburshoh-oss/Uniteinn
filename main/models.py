from django.db import models
from datetime import datetime


class UnitForm(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=13)
    SELECTED="KURSNI TANLANG"
    BACKEND="PYTHON dasturlash tili (back-end)"
    GRAFIKDIZAYN="GRAFIK DIZAYN"
    GRAFIKMODEL="GRAFIK MODELLASHTIRISH"
    FRONTEND="JAVASCRIPT dasturlash tili (front-end)"
    ROBOTOTEXNIKA="ROBOTOTEXNIKA VA MEXATRONIKA"
    SMM="SMM kursi (online marketing)"
    ANDROID="ANDROID mobil dasturlash"
    COURSES=(
        (SELECTED,SELECTED),
        (BACKEND,BACKEND),
        (GRAFIKDIZAYN,GRAFIKDIZAYN),
        (GRAFIKMODEL,GRAFIKMODEL),
        (FRONTEND,FRONTEND),
        (ROBOTOTEXNIKA,ROBOTOTEXNIKA),
        (SMM,SMM),
        (ANDROID,ANDROID)
    )
    direction=models.CharField(choices=COURSES,max_length=100)
    section=(
        ('NECHINCHI BOSQICH TALABASI','NECHINCHI BOSQICH TALABASI'),
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("O'qituvchi","O'qituvchi")
    )
    # CHOICE_TIME=(
    #     ('SIZGA QAYSI VAQT QULAY','SIZGA QAYSI VAQT QULAY'),
    #     ('ERTALAB (8-12)','ERTALAB (8-12)'),
    #     ('KECHKI (13-16)','KECHKI (13-16)'),
    #     ('KECHKI (16-21)','KECHKI (16-21)'),
    # )
    # time_managment=models.CharField(max_length=100,choices=CHOICE_TIME,null=True)
    group_number=models.CharField(max_length=10)
    course_number=models.CharField(choices=section,max_length=100)
    
    time_at=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.name