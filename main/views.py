from django.conf.urls import url
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import UnitForm
from .forms import ReceiveForm
from django.contrib import messages
from django.db.models import Q


# Create your views here.
def index_view(request):
    return render(request,"index.html")
    
def table_view(request):
    direction=request.GET.get('courses','')
    time_managment=request.GET.get('time','')
    group=request.GET.get('group','')
    query_list=Q(direction=direction) | Q(time_managment=time_managment)
    if group=='' and (direction or time_managment):
        user=UnitForm.objects.filter(query_list).order_by('-time_at')
    elif group!='':
        query_list=Q(direction=direction) | Q(time_managment=time_managment) |Q(group_number__icontains=group)
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
            if form.cleaned_data['direction']!=UnitForm.COURSES[0][0] or form.cleaned_data['time_managment']!=UnitForm.CHOICE_TIME[0][0] or form.cleaned_data['course_number']!=UnitForm.section[0][0]:
                form.save()
                return redirect('index_url')
            else:
                messages.info(request,"Iltimos kerakli maydonlarni to'ldiring")
    form=ReceiveForm()
    return render(request,'contact.html',context={'form':form})