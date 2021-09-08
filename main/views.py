from django.shortcuts import redirect, render
from .models import UnitForm
from .forms import ReceiveForm
from django.contrib import messages

# Create your views here.
def index_view(request):
    return render(request,"index.html")
    
def table_view(request):
    user=UnitForm.objects.all().order_by('-time_at')
    return render(request,'table.html',context={'users':user})


def about_view(request):
    return render(request,'about.html')

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