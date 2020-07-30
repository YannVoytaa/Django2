from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse,HttpResponseRedirect
from .models import Item
from django.urls import reverse
# Create your views here.
def home(request):
    context={
        'items':Item.objects.order_by('-pub_date')
    }
    return render(request,'base.html',context)

def new_search(request):
    text=request.POST.get('search')
    pub_date=timezone.now()
    Item.objects.create(text=text,pub_date=pub_date)
    return HttpResponseRedirect(reverse('home'))
def login(request):
    return render(request,'login/index.html')

def register(request):
    return render(request,'login/index.html')


def delete(request,item_id):
    Item.objects.get(pk=item_id).delete()
    return HttpResponseRedirect(reverse('home'))