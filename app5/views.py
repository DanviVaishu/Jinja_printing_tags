from django.shortcuts import render

def login(request):
    d={'username':'vaishu'}
    return render(request,'login.html',context=d)
