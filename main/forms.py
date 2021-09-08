
from django import forms
from .models import UnitForm


# BACKEND="BACK-END"
# GRAFIKDIZAYN="GRAFIK DIZAYN"
# GRAFIKMODEL="GRAFIK DIZAYN"
# FRONTEND="FRON-TEND"
# ROBOTOTEXNIKA="ROBOTOTEXNIKA VA MEXATRONIKA"
# COURSES=(
#     (BACKEND,BACKEND),
#     (GRAFIKDIZAYN,GRAFIKDIZAYN),
#     (GRAFIKMODEL,GRAFIKMODEL),
#     (FRONTEND,FRONTEND),
#     (ROBOTOTEXNIKA,ROBOTOTEXNIKA),
# )

# section=(
#     ("1","1"),
#     ("2","2"),
#     ("3","3"),
#     ("4","4"),
#     ("O'qituvchi","O'qituvchi")
# )
class ReceiveForm(forms.ModelForm):
    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Ism Familya'}))
    phone=forms.CharField(max_length=13,widget=forms.TextInput(attrs={'placeholder':'Tel.raqam'}))
    direction=forms.CharField(
        max_length=100,
        widget=forms.Select(choices=UnitForm.COURSES),
    )
    time_managment=forms.CharField(
        max_length=100,
        widget=forms.Select(choices=UnitForm.CHOICE_TIME),
    )
    course_number=forms.CharField(
        max_length=100,
        widget=forms.Select(choices=UnitForm.section),
    )
    group_number=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':"Guruhingizni kiriting"}))
    class Meta:
        model=UnitForm
        fields='__all__'