from django.shortcuts import render

from portfolio.helpers import age_calculator
from datetime import date


def index(request):
    context = {
        'title': 'Home',
        'banner': 'A <em>REALISTIC APPROACH</em> TO THE PROBLEM <br class="rsp-break"> BUILDING A <em>RELIABLE SOLUTION</em>.',
    }
    return render(request, 'index.html', context)


def about_me(request):
    context = {
        'title': 'About Me',
        'banner': 'My name is <em>Seongwon</em>. <br class="rsp-break"> I\'m a <em>Web Developer</em> living in Ann Arbor, MI',
        'style': 'border-top: 1px solid #fff',
        'age': age_calculator(date(1988, 2, 18))
    }
    return render(request, 'about_me.html', context)


