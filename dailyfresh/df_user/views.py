from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(requset):
	reutrn HttpResponse('<h1>hello</h1>')
