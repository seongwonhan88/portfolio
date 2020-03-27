from django.shortcuts import render

from portfolio.helpers import age_calculator
from datetime import date


def index(request):
    context = {
        'title': 'Home',
        'banner': 'A <em>REALISTIC APPROACH</em> TO THE PROBLEM <br> BUILDING A <em>RELIABLE SOLUTION</em>.',
    }
    return render(request, 'index.html', context)


def about_me(request):
    context = {
        'title': 'About Me',
        'banner': 'My name is <em>Seongwon</em> and I\'m a <em>Web Developer</em>.',
        'style': 'border-top: 1px solid #fff',
        'age': age_calculator(date(1988, 2, 18))
    }
    return render(request, 'about_me.html', context)


def skills(request):
    context = {
        'title': 'Skills',
        'banner': '<em>Languages</em> and <em>Frameworks</em>',
        'style': 'border-top: 1px solid #fff',
    }
    return render(request, 'tech_stack.html', context)
