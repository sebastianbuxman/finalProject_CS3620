from django.shortcuts import render
from .models import Clothing
from django.core.paginator import Paginator

# Create your views here.
def clothing_list(request):
    clothing_object = Clothing.objects.all()
    piece_name = request.GET.get('clothing_name')
    if piece_name != "" and piece_name is not None:
        clothing_object = clothing_object.filter(name__icontains=piece_name)
    paginator = Paginator(clothing_object, 5)
    page = request.GET.get('page')
    clothing_object = paginator.get_page(page)
    return render(request, 'lesimulatte/template.html', {'clothing_object': clothing_object})