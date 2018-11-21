from django.shortcuts import render, redirect
from .models import Registration
from .forms import SentMaill
# Create your views here.



def index(request):
    forms = SentMaill()
    if request.method == 'POST':
        forms = SentMaill(request.POST)

        if forms.is_valid():
            new_message = Registration(Email=request.POST['Email'],subject=request.POST['subject'],text=request.POST['text'])
            new_message.save()
            return redirect('Garden:index')
    else:
        forms = SentMaill()

    context = {"form":forms}
    return render(request,'Garden/index.html',context)