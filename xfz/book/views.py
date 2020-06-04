from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def book(request):
    return HttpResponse('图书首页')

def book_detail(request,book_id):
    id= request.GET.get('id')
    text='图书id{}传参是{}'.format(book_id,id)
    return HttpResponse(text)

def book_list(request):
    text ='这是图书列表'
    return HttpResponse(text)

