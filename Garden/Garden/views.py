from django.shortcuts import render, redirect
from .models import Registration, UserLists
from .forms import SentMaill, register, login
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

def registerAcount(request):
    forms = register()
    if request.method == 'POST':
        forms = register(request.POST)

        if forms.is_valid():
            new_message = UserLists(name=request.POST['text'],password=request.POST['password'],Email=request.POST['Email'])
            new_message.save()
            return redirect('Garden:index')
    else:
        forms = register()

    context = {"form":forms}
    return render(request,'Garden/registerAcount.html',context)

def loginAcount(request):
    forms = login()
    if request.method == 'POST':
        forms = login(request.POST)

        if forms.is_valid():


            return redirect('Garden:index')
    else:
        forms = login()

    context = {"form":forms}
    return render(request,'Garden/login.html',context)
