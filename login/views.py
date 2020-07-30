from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse,HttpResponseRedirect
from .models import Item, User
from django.urls import reverse
# Create your views here.
def home(request):
    try:
        user=User.objects.get(login=request.session['login'],password=request.session['password'])
        context={
            'items':user.item_set.order_by('-pub_date'),
            'user':user,
        }
    except:
        context={
            'user':None,
            'items':None,
        }
    return render(request,'base.html',context)

def new_search(request):
    text=request.POST.get('search')
    pub_date=timezone.now()
    user = User.objects.get(login=request.session['login'], password=request.session['password'])
    Item.objects.create(text=text,pub_date=pub_date,user=user)
    return HttpResponseRedirect(reverse('home'))


def login(request):
    return render(request,'login/index.html')

def register(request):
    return render(request,'login/register.html')


def delete(request,item_id):
    Item.objects.get(pk=item_id).delete()
    return HttpResponseRedirect(reverse('home'))

def verify_register(request):
    login=request.POST.get('login')
    password=request.POST.get('password')
    try:
        user=User.objects.get(login=login)
        return HttpResponse("Uzytkownik o takim loginie istnieje")
    except:
        User.objects.create(login=login,password=password)
        request.session['login']=login
        request.session['password']=password
        return HttpResponseRedirect(reverse('home'))
def verify_login(request):
    login=request.POST.get('login')
    password=request.POST.get('password')
    try:
        user=User.objects.get(login=login,password=password)
        request.session['login']=login
        request.session['password']=password
        return HttpResponseRedirect(reverse('home'))
    except:
        return HttpResponse("nie ma takiego konta")


def logout(request):
    del request.session['login']
    del request.session['password']
    return HttpResponseRedirect(reverse('home'))