from .models import Quote
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import Http404
from datetime import date
from django.utils import timezone


def index(request):

    # get today's date
    today = date.today()

    # filter Quote objects based on the current date
    quote_of_the_day = Quote.objects.filter(date_created=today)

    return render(request, 'main/index.html', { 'quotes': quote_of_the_day })

def quote_detail(request, id):
    if not isinstance(id, int):  # Check if the id is not an integer
        return render(request, 'main/404.html', status=404)

    try:
        quote_detail = Quote.objects.get(id=id)
        current_date = date.today()

        if quote_detail.date_created <= current_date:
            return render(request, "main/quote_detail.html", {"quote_detail": quote_detail})
        else:
            return render(request, 'main/404.html', status=404)
    except Quote.DoesNotExist:
        return render(request, 'main/404.html', status=404)



def past_quotes(request):
    current_date = date.today()
    past_quotes = Quote.objects.filter(date_created__lt=current_date).order_by('-date_created')
    return render(request, 'main/past_quotes.html', {'past_quotes': past_quotes})

def custom_404(request, exception=None):
    return render(request, 'main/404.html', status=404)