from django.conf.urls import url
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import UnitForm
from .forms import ReceiveForm
from django.contrib import messages
from django.db.models import Q
from .forms import ReceiveForm


# Create your views here.
def index_view(request):
    return render(request,"index.html")
    
def table_view(request):
    direction=request.GET.get('courses','')
    keyvalue=request.GET.get('keyvalue','')
    if keyvalue!='':
        print(keyvalue)
        # query_list=Q(name__contains=keyvalue)
        query_list=Q(direction__icontains=keyvalue) | Q(name__icontains=keyvalue)
        user=UnitForm.objects.filter(query_list).order_by('-time_at')
    elif direction!='':
        query_list=Q(direction=direction)
        user=UnitForm.objects.filter(query_list).order_by('-time_at')
    else:
        user=UnitForm.objects.all().order_by('-time_at')
    return render(request,'table.html',context={'users':user})


def about_view(request):
    return render(request,'about.html')

def delete_view(request,id):
    delete_user=get_object_or_404(UnitForm,pk=id)
    delete_user.delete()
    return redirect("table_url")

def register_view(request):
    if request.method=="POST":
        form=ReceiveForm(request.POST)
        if form.is_valid():
            if UnitForm.COURSES[0][0]==form.cleaned_data['direction']:
                messages.error(request, "Iltimos kursni tanlang")
            elif UnitForm.section[0][0]==form.cleaned_data['course_number']:
                messages.error(request, "Iltimos bosqichingizni tanlang")
            elif UnitForm.CHOICE_TIME[0][0]==form.cleaned_data['time_managment']:
                messages.error(request, "Iltimos kurs vaqtini tanlang tanlang")
            else:
                if  UnitForm.objects.filter(phone=form.cleaned_data['phone']).count()==0:
                    form.save()
                    messages.success(request, "Siz muvaffaqiyatli ro'yhatdan o'tdingiz. Siz bilan tez orada bog'lanamiz")
                else:
                    messages.error(request, "Siz avval ro'yhatdan o'tgansiz.")
    form=ReceiveForm()
    return render(request,'contact.html',context={'form':form})