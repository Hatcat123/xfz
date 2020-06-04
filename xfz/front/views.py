from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.

from django.shortcuts import redirect,reverse
def index(request):

    username =request.GET.get('username')
    if username:

        return HttpResponse('前台首页')
    else:
        return redirect(reverse('front:login'))

def login(request):
    return HttpResponse('前台登录页面')