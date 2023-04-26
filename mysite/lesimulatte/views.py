from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
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

def buyItems(request, clothing_id):
    #buy_items = Clothing.objects.all()
    #template = loader.get_template('lesimulatte/buyItem.html')
    clothing = get_object_or_404(Clothing, id=clothing_id)
    template = loader.get_template('lesimulatte/buyItem.html')
    context = {
        'clothing': clothing
    }
    '''context = {
        'buy_items': buy_items
    }'''
    return HttpResponse(template.render(context, request))

