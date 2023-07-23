from django.shortcuts import render, get_object_or_404
from .models import ProductModel, CategoryModel
from django.db.models import Q
# Create your views here.

def store(request, category_slug=None):
   # categories = CategoryModel.objects.all()   # eikhane oi context procossors diye calaitese 
   products = None
   
   if category_slug != None:
      category = get_object_or_404(CategoryModel, slug = category_slug)
      products = ProductModel.objects.filter(category=category, is_available = True )
   else:
      products = ProductModel.objects.all().filter(is_available = True)
   
   product_count = products.count()
   
   context = {
      'products':products , 
      'p_count':product_count, 
      }
   return render(request, 'store/store.html', context)


def product_details(request, category_slug, product_slug):
   try:
      single_product = ProductModel.objects.get(category__slug=category_slug, slug=product_slug)
   except Exception as e:
      raise e
   
   context = {
      'single_product': single_product
   }
   return render(request, 'store/product_details.html', context)


def search(request):
   if 'keyword' in request.GET:
      keyword = request.GET['keyword']
      if keyword:
         products = ProductModel.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
         product_count = products.count()
      context ={
         'products' : products,
         'p_count' : product_count,
      }
      
      return render(request, 'store/store.html', context)
