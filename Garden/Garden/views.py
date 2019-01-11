from django.shortcuts import render, redirect
from .models import Registration, UserLists
from .forms import SentMaill, Login
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

def login(request):
    forms = Login()
    if request.method == 'POST':
        forms = Login(request.POST)

        if forms.is_valid():
            new_message = UserLists(name=request.POST['text'],password=request.POST['password'],Email=request.POST['Email'])
            new_message.save()
            return redirect('Garden:index')
    else:
        forms = Login()

    context = {"form":forms}
    return render(request,'Garden/login.html',context)
