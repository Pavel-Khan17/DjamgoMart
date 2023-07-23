from django.shortcuts import render
from store.models import ProductModel

def home(request):
     product = ProductModel.objects.all()
     return render(request , 'index.html', {'products': product})