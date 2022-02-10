from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio, Hobbies


# Create your views here.
def home(request):
    return HttpResponse('<h1>About Dale</h1><br>'
                        '<hr>'
                        '<p>A little bit about myself. I am an Author and a Writer. I have my first book on '
                        'the Kindle Store. It is currently being published in paperback by Pegasus Publishing, '
                        'and will be out later this year in stores Worldwide.</p><br>'
                        '<p>Right now, I am finishing my degree in Computer Science while writing the follow-up '
                        'book to my first book. What I plan on doing with my Computer Science degree? Write '
                        'Android Apps on the side.</p>')


def hobbies(request):
    h_name = Hobbies.objects.all()
    return HttpResponse(h_name)


def portfolio(request):
    p_name = Portfolio.objects.all()
    return HttpResponse(p_name)


def contact(request):
    return HttpResponse("<h1>Dale's Contact</h2><br>"
                        "<p>daleromney@mail.weber.edu</p>")
