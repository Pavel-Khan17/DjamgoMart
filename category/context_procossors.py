from .models import CategoryModel


def manu_links(request):
   links = CategoryModel.objects.all()
   return dict(links=links)


