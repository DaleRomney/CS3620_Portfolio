from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio, Hobbies


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
    return render(request, 'PortfolioDatabase/contact.html')


def h_details(request, item_id):
    item = Hobbies.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'PortfolioDatabase/h_details.html', context)


def p_details(request, item_id):
    item = Portfolio.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'PortfolioDatabase/p_details.html', context)
