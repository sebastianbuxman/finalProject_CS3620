from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from .models import Clothing, Payment
from django.core.paginator import Paginator
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


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
    clothing_item = get_object_or_404(Clothing, id=clothing_id)
    context = {
        'clothing_item': clothing_item
    }
    return render(request, 'lesimulatte/buyItem.html', context)


def payment_view(request):
    if request.method == 'POST':
        card_holder = request.POST.get('cardHolder', '')
        card_number = request.POST.get('cardNumber', 0)
        exp_date = request.POST.get('expDate', '2022-4-27')
        cvv = request.POST.get('cvv', 0)
        payment = Payment(cardHolder=card_holder, cardNumber=card_number, expDate=exp_date, cvv=cvv)
        payment.save()

    return render(request, 'lesimulatte/payment.html')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("clothing_list")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="lesimulatte/sign_in.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("clothing_list")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="lesimulatte/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("clothing_list")
