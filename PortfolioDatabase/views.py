from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Portfolio, Hobbies, Contact
from .forms import PortfolioForm, ContactFrom


# Create your views here.
def index(request):
    return render(request, 'PortfolioDatabase/index.html')


def hobbies(request):
    h_name = Hobbies.objects.all()
    context = {
        'h_name': h_name,
    }
    return render(request, 'PortfolioDatabase/hobbies.html', context)


def portfolio(request):
    p_name = Portfolio.objects.all()
    context = {
        'p_name': p_name,
    }
    return render(request, 'PortfolioDatabase/portfolio.html', context)


def contact(request):
    c_name = Contact.objects.all()
    context = {
        'c_name': c_name,
    }
    return render(request, 'PortfolioDatabase/contact.html', context)


def h_details(request, item_id):
    item = Hobbies.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'PortfolioDatabase/h_details.html', context)


def p_details(request, item_id):
    item = Portfolio.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'PortfolioDatabase/p_details.html', context)


def add_item(request):
    form = PortfolioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('PortfolioDatabase:portfolio')

    return render(request, 'PortfolioDatabase/form.html', {'form': form})


def update_item(request, id):
    item = Portfolio.objects.get(id=id)
    form = PortfolioForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('PortfolioDatabase:portfolio')

    return render(request, 'PortfolioDatabase/form.html', {'form': form, 'item': item})


def delete_item(request, id):
    item = Portfolio.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('PortfolioDatabase:portfolio')

    return render(request, 'PortfolioDatabase/portfolio-delete.html', {'item': item})


def create_contact(request):
    form = ContactFrom(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('PortfolioDatabase:contact')

    return render(request, 'PortfolioDatabase/form.html', {'form': form})